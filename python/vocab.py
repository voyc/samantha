import configparser
import psycopg2
import sys

config = configparser.ConfigParser()
config.read('../../config.ini')

conn = psycopg2.connect(f"dbname={config['db']['name']} user={config['db']['user']} password={config['db']['password']} port={config['db']['port']}") 

for line in sys.stdin:
	t,e = line.strip().split(';')
	cur = conn.cursor()
	cur.execute("SELECT * from mai.dict d, mai.mean m where d.id = m.did and d.t = %s", (t,))
	rows = cur.fetchall()
	if cur.rowcount == 0:
		sys.stdout.write(line)
	cur.close()

conn.close()

# in ajax svc, output array is converted to json for transmit to client
# here, we build a permanent memory dict

function getvocab() {
	$a = array(
		'status' => 'system-error'
	);

	// raw inputs
	$taint_si = isset($_POST['si']) ? $_POST['si'] : 0;

	// validate inputs
	$si = validateToken($taint_si);

	// validate parameter set
	if (!$si){
		Log::write(LOG_WARNING, 'attempt with invalid parameter set');
		return $a;
	}

	// get database connection
	$conn = getConnection();
	if (!$conn) {
		return $a;
	}

	// get logged-in user
	$result = getUserByToken($conn, $si);
	if (!$result) {
		return $a;
	}
	$row = pg_fetch_array($result, 0, PGSQL_ASSOC);
	$userid = $row['id'];

	// read vocab for logged-in user
	$name = 'query-vocab';
	$sql = "select word, type, state, mastery, recency from mai.vocab where userid = $1";
	$params = array($userid);
	$result = execSql($conn, $name, $sql, $params, false);
	if (!$result) {
                return $a;
	}

        // build array of vocab words
        $vocabs = array();
        $numrows = pg_num_rows($result);
        for ($i=0; $i<$numrows; $i++) {
                $row = pg_fetch_array($result, $i, PGSQL_ASSOC);
                $vocab = array();
		$vocab['w'] = $row['word'];
		$vocab['t'] = $row['type'];
		$vocab['s'] = $row['state'];
		$vocab['m'] = $row['mastery'];
		$vocab['r'] = $row['recency'];
                $vocabs[] = $vocab;
        }


	// success
	$a['status'] = 'ok';
	$a['list'] = $vocabs;
	return $a;
}


?>
/**
	class Vocab
	singleton
	Maintain a list of vocabulary words, in db and in localStorage.
	Each entry in the list looks like this:
		{
			w:'กิน', // word
			s:'m',  // state w/t/u/r/m
			m:0,    // mastery
			r:5702539857129 // recency timestamp
			t:'g'   // type g/w/l
		}
**/
voyc.Vocab = function() {
	var self = this;
	voyc.observer.subscribe('login-received'   ,'user' ,function(note) { self.onLoginReceived   (note);});
	voyc.observer.subscribe('relogin-received'   ,'user' ,function(note) { self.onReloginReceived   (note);});
	voyc.observer.subscribe('getvocab-received'   ,'user' ,function(note) { self.onVocabReceived   (note);});
	
	this.language = 'th';
	this.timerid = null;
	this.vocab = {};
	this.frozen = false;
}

voyc.Vocab.prototype.onLoginReceived = function(note) {
	this.vocab = this.removeSto();
	this.vocab = this.retrieveSto();
	this.readServer();
}

voyc.Vocab.prototype.onReloginReceived = function(note) {
	this.vocab = this.retrieveSto();
	this.readServer();
}

voyc.Vocab.prototype.iterate = function(cb) {
	for (var i=0; i<this.vocab.list.length; i++) {
		voc = this.vocab.list[i];
		cb(voc,i);
	}
}

voyc.Vocab.prototype.onVocabReceived = function(note) {
	var serverList = note.payload.list;
	var localList = this.vocab.list;

	// fix serverList types
	for (var i=0; i<serverList.length; i++) {
		serverList[i].m = parseInt(serverList[i].m);
		serverList[i].r = parseInt(serverList[i].r);
	}

	function findInServerList(word) {
		for (var i=0; i<serverList.length; i++) {
			if (serverList[i].w == word) {
				return serverList[i];
			}
		}
		return false;
	}

	function findInLocalList(word) {
		for (var i=0; i<localList.length; i++) {
			if (localList[i].w == word) {
				return localList[i];
			}
		}
		return false;
	}

	// loop thru local list
	var dirtyBatch = [];
	for (var i=0; i<localList.length; i++) {
		var x = localList[i];
		var m = findInServerList(x.w);
		if (m && m.recency > x.r) {
			x.m = m.m;
			x.s = m.s;
			x.r = m.r;
		}
		if (!m || m.recency < x.r) {
			dirtyBatch.push(x);
		}
	}

	// loop thru server list
	for (var i=0; i<serverList.length; i++) {
		var m = findInLocalList(serverList[i].w);
		if (!m) {
			localList.push(serverList[i]);
		}
	}
	this.updateServer(dirtyBatch);
	this.storeSto();
	this.vocab.recency = Date.now();

	this.vocab.list.sort(function(a,b) {
		return (a.r - b.r);
	});
}

voyc.Vocab.prototype.setDirty = function() {
	if (!this.timerid) {
		var self = this;
		this.timerid = setTimeout( function() {
			self.updateServer(self.prepDirtyBatch());
			self.timerid = null;
		}, (10*1000));
	}
}

voyc.Vocab.prototype.prepDirtyBatch = function() {
	var dirtyBatch = [];
	var newrecency = Date.now();
	for (var i=0; i<this.vocab.list.length; i++) {
		var m = this.vocab.list[i];
		if (m.r > this.vocab.recency) {
			dirtyBatch.push(m);
		}
	}
	this.vocab.recency = newrecency;
	return dirtyBatch;
}

voyc.Vocab.prototype.updateServer = function(dirtyBatch) {
	var svcname = 'setvocab';
	if (dirtyBatch.length <= 0) {
		return;
	}
	var list = JSON.stringify(dirtyBatch);

	// build data array of name/value pairs from user input
	var data = {};
	data['si'] = voyc.getSessionId();
	data['list'] = list;
	data['language' ] = this.language;

	// call svc
	voyc.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		voyc.observer.publish('setvocab-received', 'mai', response);

		if (response['status'] == 'ok') {
			console.log('setvocab success');
		}
		else {
			console.log('setvocab failed');
		}
	});

	voyc.observer.publish('setvocab-posted', 'mai', {});
}

voyc.Vocab.prototype.readServer = function() {
	var svcname = 'getvocab';

	// build data array of name/value pairs from user input
	var data = {};
	data['si'] = voyc.getSessionId();
	data['language' ] = this.language;

	// call svc
	voyc.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		voyc.observer.publish('getvocab-received', 'mai', response);

		if (response['status'] == 'ok') {
			console.log('getvocab success');
		}
		else {
			console.log('getvocab failed');
		}
	});

	voyc.observer.publish('getvocab-posted', 'mai', {});
}

voyc.Vocab.prototype.storeSto = function() {
	localStorage.setItem('vocab', JSON.stringify(this.vocab));
	this.setDirty();
}

voyc.Vocab.prototype.removeSto = function() {
	localStorage.removeItem('vocab');
}

voyc.Vocab.prototype.retrieveSto = function() {
	var vocab = JSON.parse(localStorage.getItem('vocab'));
	if (!vocab) {
		vocab = {
			lang: this.language,
			recency: Date.now(),
			list: []
		};
	}
	return vocab;
}

/**
	remove - remove one entry from the list
	@input {string} word
**/	
voyc.Vocab.prototype.remove = function(word) {
	for (var i=0; i<this.vocab.list.length; i++) {
		var e = this.vocab.list[i];
		if (e.w == word) {
			this.vocab.list.splice(i,1);
			break;
		}
	}
	if (!this.frozen) {
		this.storeSto();
	}
}

/**
	get - read one entry from the list
	@input {string} word
	@return {object}
**/	
voyc.Vocab.prototype.get = function(word) {
	var r = false;
	for (var i=0; i<this.vocab.list.length; i++) {
		var e = this.vocab.list[i];
		if (e.w == word) {
			r = e;
			break;
		}
	}
	return r;
}

/**
	set
	insert or update one entry into the list
	@input {string} word
	@input {string} state
	@return {number} count of new entries inserted
**/	
voyc.Vocab.prototype.set = function(word, type, state) {
	if (!word) {
		//debugger;
	}
	var mastery = (state == 'm') ? 1 : 0;
	var e = this.get(word);
	if (e) {
		e.s = state;
		e.r = Date.now();
		e.m += mastery;
	}
	else {
		this.vocab.list.push({w:word,t:type,s:state,r:Date.now(),m:mastery});
	}
	if (!this.frozen) {
		this.storeSto();
	}
}

/**
	getlist - return an array of entries
	@input {string} state
	@return {array}
**/	
voyc.Vocab.prototype.getlist = function(state, type) {
	var r = [];
	for (var i=0; i<this.vocab.list.length; i++) {
		var e = this.vocab.list[i];
		if ((e.s == state || !state) && (e.t == type || !type)) {
			r.push(e);
		}
	}
	return r;
}

/**
	finger - update the recency timestamp
	@input {string} word
	@input {number} timestamp
	@return null
**/
voyc.Vocab.prototype.finger = function(word, recency) {
	var e = this.get(word);
	if (e) {
		e.r = recency;
	}
	else {
		if (voyc.analyticLogging) 
			console.log(['finger vocab word not found', word]);
	}
	if (!this.frozen) {
		this.storeSto();
	}
}

voyc.Vocab.prototype.freeze = function() {
	this.frozen = true;
}

voyc.Vocab.prototype.thaw = function() {
	this.frozen = false;
	this.retrieveSto();
}
