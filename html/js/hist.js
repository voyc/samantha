/**
	class Hist
	@constructor
	singleton

	querystring, url, bookmark are equivalent

	state is an object version of the querystring

	querystring format:
		"?page=genghis&view=birdseye&section=photo"

	state format:
		{page:'genghis',view:'birdseye',section:'photo'}

	the windows.history.pushState() method uses both formats

	the application uses only the state format

**/
voyc.Hist = function(onNavCallback) {
	// is singleton
	if (voyc.Hist._instance) return voyc.Hist._instance;
	else voyc.Hist._instance = this;

	this.onNavCallback = onNavCallback;
	this.starturl = window.location.search;

	var self = this;
	window.addEventListener('popstate', function(event) {
		self.onNavCallback(event['state']);
	}, false);
}

// public method called by app to navigate to a new page
voyc.Hist.prototype.nav = function(state) {
	var state = state || this.parseQueryString(this.starturl);
		
	if (!(window.location.protocol.indexOf('file') > -1)) {
		var url = this.composeQueryString(state);
		window.history.pushState(state, '', url);
	}
	this.onNavCallback(state);
}

// utility method converts format querystring to state
voyc.Hist.prototype.parseQueryString = function(querystring) {
	var state = {};
	var a = querystring.substr(1).split('&');
	for (var i=0; i<a.length; i++) {
		var b = a[i].split('=');
		state[b[0]] = b[1];
	}
	return state;
}

// utility method converts format state to querystring
voyc.Hist.prototype.composeQueryString = function(state) {
	var querystring = '';
	var ks = Object.keys(state);
	for (var i=0; i<ks.length; i++) {
		var k = ks[i];
		var v = state[k];
		querystring += (querystring.length) ? '&' : '?'; 
		querystring += k + '=' + v;
	}
	return querystring;
}

