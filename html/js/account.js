/**
 * class voyc.Account
 * @constructor
 * A singleton object
 * Manages user authentication.

 Values returned in response.
              session     screen
	status      no          no
	si          yes         no
	auth        yes         yes
	access      yes         no
	uname       no          yes
	email       no          no

 Object voyc.Account handles sessionStorage.
 Object voyc.AccountView handles display to screen.

 */
voyc.Account = function () {
	if (voyc.Account._instance) return voyc.Account._instance;
	voyc.Account._instance = this;

	this.observer = new voyc.Observer();
	
	var url = '/account/svc.php';
	if (window.location.origin == 'file://' || window.location.port == '8080') {
		url = 'http://samantha.voyc.com/account/svc.php';  // for local testing
	}
	this.comm = new voyc.Comm(url, 'acomm', 2, true);

	// attach app events
	var self = this;
	this.observer.subscribe('setup-complete'           ,'account' ,function(note) { self.onSetupComplete           (note); });
	this.observer.subscribe('login-submitted'          ,'account' ,function(note) { self.onLoginSubmitted          (note); });
	this.observer.subscribe('logout-requested'         ,'account' ,function(note) { self.onLogoutRequested         (note); });
	this.observer.subscribe('register-submitted'       ,'account' ,function(note) { self.onRegisterSubmitted       (note); });
	this.observer.subscribe('verify-submitted'         ,'account' ,function(note) { self.onVerifySubmitted         (note); });
	this.observer.subscribe('forgotpassword-submitted' ,'account' ,function(note) { self.onForgotPasswordSubmitted (note); });
	this.observer.subscribe('resetpassword-submitted'  ,'account' ,function(note) { self.onResetPasswordSubmitted  (note); });
	this.observer.subscribe('changepassword-submitted' ,'account' ,function(note) { self.onChangePasswordSubmitted (note); });
	this.observer.subscribe('changeusername-submitted' ,'account' ,function(note) { self.onChangeUsernameSubmitted (note); });
	this.observer.subscribe('changeemail-submitted'    ,'account' ,function(note) { self.onChangeEmailSubmitted    (note); });
	this.observer.subscribe('verifyemail-submitted'    ,'account' ,function(note) { self.onVerifyEmailSubmitted    (note); });
}

voyc.Account.svcdef = {
	'register':       {'uname':1, 'email':1, 'pword':1, 'both':0, 'pnew':0, 'si':0, 'tic':0},
	'verify':         {'uname':0, 'email':0, 'pword':1, 'both':0, 'pnew':0, 'si':1, 'tic':1},
	'login':          {'uname':0, 'email':0, 'pword':1, 'both':1, 'pnew':0, 'si':0, 'tic':0},
	'relogin':        {'uname':0, 'email':0, 'pword':0, 'both':0, 'pnew':0, 'si':0, 'tic':0},
	'logout':         {'uname':0, 'email':0, 'pword':0, 'both':0, 'pnew':0, 'si':1, 'tic':0},
	'forgotpassword': {'uname':0, 'email':0, 'pword':0, 'both':1, 'pnew':0, 'si':0, 'tic':0},
	'resetpassword':  {'uname':0, 'email':0, 'pword':0, 'both':0, 'pnew':1, 'si':1, 'tic':1},
	'changepassword': {'uname':0, 'email':0, 'pword':1, 'both':0, 'pnew':1, 'si':1, 'tic':0},
	'changeusername': {'uname':1, 'email':0, 'pword':1, 'both':0, 'pnew':0, 'si':1, 'tic':0},
	'changeemail':    {'uname':0, 'email':1, 'pword':1, 'both':0, 'pnew':0, 'si':1, 'tic':0},
	'verifyemail':    {'uname':0, 'email':0, 'pword':1, 'both':0, 'pnew':0, 'si':1, 'tic':1},
}

voyc.Account.fielddef = {
	'uname':	{'type':'text'    , 'valuetype':'value'  , 'display':'username'},
	'email':	{'type':'text'    , 'valuetype':'value'  , 'display':'email'},
	'pword':	{'type':'text'    , 'valuetype':'value'  , 'display':'password'},
	'both':		{'type':'text'    , 'valuetype':'value'  , 'display':'username or email'},
	'pnew':		{'type':'text'    , 'valuetype':'value'  , 'display':'new password'},
	'si':		{'type':'text'    , 'valuetype':'value'  , 'display':'session-id'},
	'tic':		{'type':'text'    , 'valuetype':'value'  , 'display':'temporary id code'},
}

/* 
	user authentication states
		database, svc, sessionStorage use numeric
		javascript programming uses string, getAuth() 
*/
voyc.Account.authdef = {
	0: 'anonymous'   ,
	1: 'registered'  ,
	2: 'resetpending',
	7: 'verified'    ,  // auth >= verified vs auth < verified
	8: 'emailpending',
}
voyc.Account.svcbyauth = {
	'register':       {'anonymous':1, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':0 },
	'verify':         {'anonymous':0, 'registered':1, 'resetpending':0, 'emailpending':0, 'verified':0 },
	'login':          {'anonymous':1, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':0 },
	'relogin':        {'anonymous':0, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':0 },
	'logout':         {'anonymous':0, 'registered':1, 'resetpending':1, 'emailpending':1, 'verified':1 },
	'forgotpassword': {'anonymous':1, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':0 },
	'resetpassword':  {'anonymous':0, 'registered':0, 'resetpending':1, 'emailpending':0, 'verified':0 },
	'changepassword': {'anonymous':0, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':1 },
	'changeusername': {'anonymous':0, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':1 },
	'changeemail':    {'anonymous':0, 'registered':0, 'resetpending':0, 'emailpending':0, 'verified':1 },
	'verifyemail':    {'anonymous':0, 'registered':0, 'resetpending':0, 'emailpending':1, 'verified':1 },
}

voyc.Account.accessdef = {
	   0: 'none',
	   1: 'novice',
	 100: 'pro',
	 200: 'master',
	 235: 'admin',
	 255: 'super'
}

/* services */

voyc.Account.prototype.onLoginSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}
		self.observer.publish('login-received', 'account', response);
		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.requestPending(response);
		}
	});

	this.observer.publish('login-posted', 'account', {});
}

voyc.Account.prototype.onRegisterSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('register-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.requestPending(response);
			self.assertAuth('registered');
		}
	});

	this.observer.publish('register-posted', 'account', {});
}

voyc.Account.prototype.onVerifySubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('verify-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.assertAuth( 'verified');
		}
	});

	this.observer.publish('verify-posted', 'account', {});
}

voyc.Account.prototype.onSetupComplete = function(note) {
	if (voyc.getSessionId()) {
		var svcname = 'relogin';
		var data = { 'si':voyc.getSessionId() };
		var self = this;
		this.comm.request(svcname, data, function(ok, response, xhr) {
			if (!ok) {
				response = { 'status':'system-error'};
			}
			self.observer.publish('relogin-received', 'account', response);
			if (response['status'] == 'ok') {
				self.saveSession(response);
				self.requestPending(response);
			}
			else {
				console.log('relogin failed.  session cleared.');
				self.clearSession();
			}
		});
		this.observer.publish('relogin-posted', 'account', {});
	}
	else {
		this.clearSession();
		this.observer.publish('restart-anonymous', 'account', {});
	}
}

voyc.Account.prototype.onLogoutRequested = function(note) {
	// post to svc
	var svcname = 'logout';
	var data = { 'si':voyc.getSessionId() };
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}
		self.clearSession();
		self.observer.publish('logout-received', 'account', response);
	});

	this.observer.publish('logout-posted', 'account', {});
}

voyc.Account.prototype.onForgotPasswordSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('forgotpassword-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.assertAuth('resetpending');
			self.observer.publish('resetpassword-requested', 'account', response);
		}
		else {
			self.clearSession();
		}
	});

	this.observer.publish('forgotpassword-posted', 'account', {});
}

voyc.Account.prototype.onResetPasswordSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('resetpassword-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.assertAuth('verified');
		}
	});

	this.observer.publish('resetpassword-posted', 'account', {});
}

voyc.Account.prototype.onChangePasswordSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('changepassword-received', 'account', response);

		if (response['status'] == 'ok') {
			console.log('change password successful');
		}
	});

	this.observer.publish('changepassword-posted', 'account', {});
}

voyc.Account.prototype.onChangeUsernameSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('changeusername-received', 'account', response);

		if (response['status'] == 'ok') {
			console.log('change username successful');
		}
	});

	this.observer.publish('changeusername-posted', 'account', {});
}

voyc.Account.prototype.onChangeEmailSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('changeemail-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.requestPending();
			self.assertAuth('emailpending');
		}
	});

	this.observer.publish('changeemail-posted', 'account', {});
}
voyc.Account.prototype.onVerifyEmailSubmitted = function(note) {
	var svcname = note.payload.svc;
	var inputs = note.payload.inputs;

	// build data array of name/value pairs from user input
	var data = this.buildDataArray(svcname, inputs);

	// call svc
	var self = this;
	this.comm.request(svcname, data, function(ok, response, xhr) {
		if (!ok) {
			response = { 'status':'system-error'};
		}

		self.observer.publish('verifyemail-received', 'account', response);

		if (response['status'] == 'ok') {
			self.saveSession(response);
			self.assertAuth('verified');
		}
	});


	this.observer.publish('verifyemail-posted', 'account', {});
}

/* utilities */

voyc.Account.prototype.buildDataArray = function(svcname, inputs) {
	var data = {};
	var fields = voyc.Account.svcdef[svcname];
	for (var name in fields) {
		var req = fields[name];
		var valuetype = voyc.Account.fielddef[name]['valuetype'];
		if (req) {
			var value = '';
			if (name == 'si') {
				value = voyc.getSessionId();
			}
			else {
				value = inputs[name][valuetype];
				if (valuetype == 'checked') {
					value = (value) ? 't' : 'f';
				}
			}
			data[name] = value;
		}
	}
	return data;
}

voyc.Account.prototype.isSvcAllowed = function(svc) {
	return 	this.isSvcAllowedForAuth(svc, this.getAuth());
}

voyc.Account.prototype.isSvcAllowedForAuth = function(svc, auth) {
	return voyc.Account.svcbyauth[svc][auth];
}

voyc.Account.prototype.getAllowedSvcsForAuth = function(auth) {
	var list = [];
	for (var svc in voyc.Account.svcbyauth) {
		if (voyc.Account.svcbyauth[svc][auth]) {
			list.push(svc);
		}
	}
	return [];
}

voyc.Account.prototype.getAuth = function() {
	var code = voyc.Session.get('auth');
	return voyc.Account.authdef[code];
}

voyc.Account.prototype.assertAuth = function(auth) {
	if (this.getAuth() != auth) {
		console.log('assertion failed.  auth is not ' + auth)
	}
}

voyc.Account.prototype.saveSession = function(response) {
	if (response['si'])     voyc.Session.set('si', response['si']);
	if (response['auth'])   voyc.Session.set('auth', response['auth']);
	if (response['access']) voyc.Session.set('access', response['access']);
}

voyc.Account.prototype.clearSession = function() {
	voyc.Session.set('si', '');
	voyc.Session.set('auth', '0');
	voyc.Session.set('access', '0');
}

voyc.Account.prototype.requestPending = function(response) {
 	if (voyc.isUserRegistered()) {
		this.observer.publish('verify-requested', 'account', response);
	}
	if (voyc.isUserEmailPending()) {
		this.observer.publish('verifyemail-requested', 'account', response);
	}
	if (voyc.isUserResetPending()) {
		this.observer.publish('resetpassword-requested', 'account', response);
	}
}

/*  global functions */

voyc.isSvcAllowed = function(svc) { return (new voyc.Account).isSvcAllowed(svc); }
voyc.getAuth = function() { return (new voyc.Account).getAuth(); }
voyc.isUserAnonymous   = function() { return voyc.getAuth() == 'anonymous'   ;}
voyc.isUserRegistered  = function() { return voyc.getAuth() == 'registered'  ;}
voyc.isUserResetPending= function() { return voyc.getAuth() == 'resetpending';}
voyc.isUserVerified    = function() { return voyc.getAuth() == 'verified'    ;}
voyc.isUserEmailPending= function() { return voyc.getAuth() == 'emailpending';}
voyc.getSessionId = function() { return voyc.Session.get('si'); }
