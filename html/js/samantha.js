/**
	class voyc.Samantha
	@constructor
	A singleton object
*/
voyc.Samantha = function () {
	if (voyc.Samantha._instance) return voyc.Samantha._instance;
	voyc.Samantha._instance = this;
	this.setup();
}

voyc.Samantha.prototype.setup = function () {
	// url for server communications
	var url = '/svc/';
	if (window.location.origin == 'file://' || window.location.port == '8080') {
		url = 'http://samantha.voyc.com/svc';  // for local testing
	}

	// instantiate user management
	new voyc.User();
	new voyc.Account();
	new voyc.AccountView();

	// instantiate utilities
	voyc.comm = new voyc.Comm(url, 'mcomm', 2, true);
	voyc.observer = new voyc.Observer();
	voyc.speech = new voyc.Speech();

	// instantiate controller, navigation via browser history
	voyc.view = new voyc.View();
	voyc.hist = new voyc.Hist(function(state) {
		var event = state.page;
		voyc.observer.publish(event+'-requested', 'mai', {state});
	});

	// instantiate chat
	this.chat = new voyc.Chat();
	this.chat.setup(document.getElementById('chatcontainer'));

	// attach app events
	var self = this;

	voyc.observer.publish('setup-complete', 'samantha', {});
	voyc.hist.nav({page:'home'});
	
	window.addEventListener('resize', function() {
		self.resize();
	}, false);
	this.resize();
}

voyc.Samantha.prototype.resize = function() {
}

/* on startup */
window.addEventListener('load', function(evt) {
	voyc.samantha = new voyc.Samantha();
}, false);

