// अथ योगानुशासनम्॥१॥
/**
	class voyc.User
	@constructor
	Singleton object.
	Represents the current user.
	May be logged-in or anonymous.
*/
voyc.User = function() {
	this.username = '';
	this.auth = '';
	this.access = '';

	this.observer = new voyc.Observer();

	var self = this;
	this.observer.subscribe('login-received'   ,'user' ,function(note) { self.onLoginReceived   (note);});
	this.observer.subscribe('logout-received'  ,'user' ,function(note) { self.onLogoutReceived  (note);});
}

voyc.User.prototype.isAnonymous = function() {
	return (!this.username);
}

voyc.User.prototype.onLoginReceived = function(note) {
	this.username = note.payload['uname'];
	this.auth = note.payload['auth'];
	this.access = note.payload['access'];
}

voyc.User.prototype.onLogoutReceived = function(note) {
	this.username = '';
	this.auth = '';
	this.access = '';
}
