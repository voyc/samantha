/**
 * class voyc.View
 * @constructor
 * A singleton object
 */
voyc.View = function () {
	if (voyc.View._instance) return voyc.View._instance;
	voyc.View._instance = this;
	this.setup();
}

voyc.View.prototype.setup = function () {
	this.observer = new voyc.Observer();

	// attach handlers to HTML elements in the base html
	this.attachHandlers();

	// attach app events
	var self = this;
	//this.observer.subscribe('home-requested'         ,'view' ,function(note) { self.drawPage('home');    });
	//this.observer.subscribe('about-requested'        ,'view' ,function(note) { self.drawPage('about');   });
	//this.observer.subscribe('account-requested'      ,'view' ,function(note) { self.drawPage('account'); });
	//this.observer.subscribe('profile-requested'      ,'view' ,function(note) { self.drawPage('profile'); self.clearProfileForm(); });
}

/**
**/
voyc.View.prototype.attachHandlers = function(element) {
	var elem = element || document;

	// click on a nav item
	var self = this;
	var navs = elem.querySelectorAll('[nav]');
	for (var i=0; i<navs.length; i++) {
		navs[i].addEventListener('click', function(e) {
			var pageid = e.currentTarget.getAttribute('nav');
			//self.observer.publish('nav-requested', 'view', {page:pageid});
			(new voyc.BrowserHistory).nav(pageid);
		}, false);
	}

	// attach click handlers to the submit buttons in the header and dialogs
	var elems = elem.querySelectorAll('[type=submit]');
	var e, dialog;
	var self = this;
	for (i=0; i<elems.length; i++) {
		e = elems[i];
		dialog = voyc.findParentWithTag(e, 'form');
		dialog.addEventListener('submit', function(evt) {
			evt.preventDefault();
			self.onSubmitClick(evt);
		}, false);
	}
}

// dialog submit button has been clicked
voyc.View.prototype.onSubmitClick = function(evt) {
	var form = evt.currentTarget;
	var svc = form.id;
	var inputs = form.elements;
	var note = svc + '-submitted';
	this.observer.publish(note, 'view', {svc:svc, inputs:inputs});
	voyc.$('dialog-msg').innerHTML = '';
}

voyc.View.prototype.drawPage = function(pageid) {
	voyc.hide('content-home'   );
	voyc.hide('content-about'  );
	voyc.hide('content-profile');
	voyc.show('content-'+pageid);
}

voyc.View.prototype.clearProfileForm = function() {
	voyc.$('gender').value = '';
	voyc.$('photo' ).value = '';
	voyc.$('phone' ).value = '';
}
