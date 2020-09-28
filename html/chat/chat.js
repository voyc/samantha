/**
	class Chat
	@constructor
**/
voyc.Chat = function() {
	this.chatcontainer = {};
	this.chatscroller = {};
	this.chatcontent = {};
	this.eEntry = {};
	this.ws = false;
	this.username = '';

	this.port = 8080
	this.ip = '68.66.224.22'
	//this.ip = '127.0.0.1'
}

voyc.Chat.containertemplate = `
	<div id='chatscroller'>
		<div id='chatcontent'></div>
	</div>
	<div id='chatfoot'>
		<table id='chatentry' class='chatentry'>
			<td><textarea id='mmsg'></textarea></td>
			<td><div id='mchoices'>yes no</div></td>
			<td><button id='mbtn'>></button></td>
		</table>
	</div>
`;

voyc.Chat.linetemplate = `
	<div class='chatline clearfix'>
		<div class='chatuser f%side%'>%user%</div>
		<div class='chatmsg f%side%'>%message%</div>
		<div class='chattime f%side%'>%time%</div>
	</div>
`;

voyc.Chat.loginblock = `
	<p>Click here for <a href=wiki/doku.php>Wiki</a></p>
	<p>Connecting to chat server...<span id=spanconnect class=hidden> Connected</span><span id=spanconnectfail class=hidden> Failed</span></p>
	<p id=loginline class=hidden>Username: <input id=loginusername/><button id=loginbtn>Login</button><p>
`;

voyc.Chat.prototype.setup = function(container) {
	this.chatcontainer = container;
	this.chatcontainer.innerHTML = voyc.Chat.containertemplate;
	this.chatscroller = document.getElementById('chatscroller');
	this.chatcontent = document.getElementById('chatcontent');

	var self = this;
	document.getElementById('mbtn').addEventListener('click', function(e) {
		var s = document.getElementById('mmsg').value;
		voyc.chat.post(s, false)
		document.getElementById('mmsg').value = '';
	}, false);
	document.getElementById('mmsg').addEventListener('keydown', function(e) {
		if (e.keyCode == 13) {
			document.getElementById('mbtn').click();
			e.preventDefault();
		}
	}, false);

	this.displayhard(voyc.Chat.loginblock);

	document.getElementById('loginbtn').addEventListener('click', function(e) {
		voyc.chat.login();
		voyc.chat.loginblock.classList.add('hidden');
	}, false);

	//this.ws = new WebSocket("ws://68.66.224.22:5678/");
	var addr = 'ws://'+this.ip+':'+this.port+'/';
	console.log('open connection to '+addr);
	this.ws = new WebSocket(addr);
	this.ws.onmessage = function (event) {
		var a = event.data.split('~')
		user = a[0];
		message = a[1];
		voyc.chat.display(user, message, false);
	};
	this.ws.onopen = function (event) {
		console.log('opened');
		document.getElementById('spanconnect').classList.remove('hidden');
		document.getElementById('loginline').classList.remove('hidden');
	};
	this.ws.onclose = function (event) {
		console.log('close');
	};
	this.ws.onerror = function (event) {
		console.log('error');
		document.getElementById('spanconnectfail').classList.remove('hidden');
	};
}

voyc.Chat.prototype.resize = function(height) {
	this.chatscroller.style.height = height - document.getElementById('chatfoot').offsetHeight + 'px';
}

voyc.Chat.prototype.login = function() {
	name = prompt('What is your name?', 'John');
	this.username = document.getElementById('loginusername').value;	
	this.ws.send('login~'+this.username+'~')
}

voyc.Chat.prototype.post = function(message, mchoice) {
	//this.display(this.username, message, mchoice);
	msg = 'message~' + this.username + '~' + message
	this.ws.send(msg)
}

voyc.Chat.prototype.displayhard = function(s) {
	var m = document.createElement('div');
	m.innerHTML = s;
	this.chatcontent.appendChild(m);

	this.chatscroller.scrollTop = this.chatscroller.scrollHeight;
	document.getElementById('mmsg').focus();
}

voyc.Chat.prototype.display = function(username, message, mchoice) {
	var side = 'right';
	var name = '';
	if (username != this.username) {
		side = 'left';
		name = username + ':';
	}

	var dtime = new Date();
	var hh = dtime.getHours();
	var mm = dtime.getMinutes();
	var smm = mm.toString();
	smm = (smm.length > 1) ? smm : '0' + smm;
	var stime = hh + ':' + smm;

	// add message box to chat box
	var s = voyc.Chat.linetemplate;
	s = s.replace(/[\n\t]/g,'');
	s = s.replace(/%side%/g, side);
	s = s.replace(/%user%/g, name);
	s = s.replace(/%message%/g, message);
	s = s.replace(/%time%/g, stime);

	var m = document.createElement('div');
	m.innerHTML = s;
	this.chatcontent.appendChild(m);

	this.chatscroller.scrollTop = this.chatscroller.scrollHeight;
	document.getElementById('mmsg').focus();

	// add multiple choice options
	var self = this;
	var soptions = '';
	document.getElementById('mchoices').innerHTML = '';
	if (mchoice) {
		for (var i=0; i<mchoice.length; i++) {
			var opt = document.createElement('button');
			opt.id = 'opt_' + i;
			opt.innerHTML = mchoice[i];
			document.getElementById('mchoices').appendChild(opt);
			opt.addEventListener('click', function(e) {
				var s = e.target.innerHTML;
				self.display(this.username,s);
			}, false);
		}
	}

	return m;
}
