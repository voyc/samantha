/**
	class AccountView
	@constructor
	Singleton object.
	Represents the header and modal dialogs for account events.
*/
voyc.AccountView = function() {
	this.observer = new voyc.Observer();
	this.uname = '';

	// there are nine account events with modal dialogs
	// on a request, open a modal dialog
	var self = this;
	this.observer.subscribe('login-requested'          ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('login');          });
	this.observer.subscribe('register-requested'       ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('register');       });
	this.observer.subscribe('verify-requested'         ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('verify');         });
	this.observer.subscribe('forgotpassword-requested' ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('forgotpassword'); });
	this.observer.subscribe('resetpassword-requested'  ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('resetpassword');  });
	this.observer.subscribe('changepassword-requested' ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('changepassword'); });
	this.observer.subscribe('changeusername-requested' ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('changeusername'); });
	this.observer.subscribe('changeemail-requested'    ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('changeemail');    });
	this.observer.subscribe('verifyemail-requested'    ,'accountview' ,function(note) { (new voyc.Minimal).openPopup('verifyemail');    });

	// when svc posted to server, put dialog in wait state
	this.observer.subscribe('login-posted'             ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('register-posted'          ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('verify-posted'            ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('forgotpassword-posted'    ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('resetpassword-posted'     ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('changepassword-posted'    ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('changeusername-posted'    ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('changeemail-posted'       ,'accountview' ,function(note) { self.modalWait(note);});
	this.observer.subscribe('verifyemail-posted'       ,'accountview' ,function(note) { self.modalWait(note);});

	// when the svc returns form server, clear the wait state, close the dialog, enable/disable request buttons depending on new auth status
	this.observer.subscribe('login-received'           ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('register-received'        ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('verify-received'          ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('forgotpassword-received'  ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('resetpassword-received'   ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('changeusername-received'  ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('changeemail-received'     ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('verifyemail-received'     ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});
	this.observer.subscribe('changepassword-received'  ,'accountview' ,function(note) { self.closeModal(note); self.refresh(note);});

	// these three events have no dialog
	this.observer.subscribe('logout-received'          ,'accountview' ,function(note) { self.refresh(note);});
	this.observer.subscribe('restart-anonymous'        ,'accountview' ,function(note) { self.refresh(note);});
	this.observer.subscribe('relogin-received'         ,'accountview' ,function(note) { self.refresh(note);});

//	// attach click handlers to the submit buttons in the header and dialogs
//	var elems = document.querySelectorAll('[type=submit]');
//	var elem, dialog;
//	var self = this;
//	for (i=0; i<elems.length; i++) {
//		elem = elems[i];
//		dialog = voyc.findParentWithTag(elem, 'form');
//		dialog.addEventListener('submit', function(evt) {
//			evt.preventDefault();
//			self.onSubmitClick(evt);
//		}, false);
//	}
//
	// attach click handlers to the request buttons in the header and dialogs
	var elems = document.querySelectorAll('[request]');
	var elem;
	var self = this;
	for (i=0; i<elems.length; i++) {
		elem = elems[i];
		elem.addEventListener('click', function(evt) {
			var name = evt.currentTarget.getAttribute('request') + '-requested';
			self.observer.publish(name, 'accountview', {});
		}, false);
	}
}

// dialog submit button has been clicked
voyc.AccountView.prototype.onSubmitClick = function(evt) {
	var form = evt.currentTarget;
	var svc = form.id;
	var inputs = form.elements;
	var note = svc + '-submitted';
	this.observer.publish(note, 'accountview', {svc:svc, inputs:inputs});
	voyc.$('dialog-msg').innerHTML = '';
}

// put modal dialog into a wait state
voyc.AccountView.prototype.modalWait = function(note) {
	voyc.wait();
}

// clear wait state and close modal dialog
voyc.AccountView.prototype.closeModal = function(note) {
	if (note.payload['status'] == 'ok') {
		voyc.closePopup();
	}
	else {
		voyc.killWait();
		voyc.$('dialog-msg').innerHTML = note.payload['status'];
	}
}

// refresh the header and dialogs
voyc.AccountView.prototype.refresh = function(note) {
	this.uname = note.payload['uname'] || '';

	// refresh header
	var x = voyc.getAuth();
	switch (x) {
		case 'anonymous'   :
			voyc.$('loggedinuser').innerHTML = '';
			voyc.$('headeruser').style.display = 'table-cell';
			voyc.$('headerlogin').style.display = 'inline-block';
			voyc.$('headerlogout').style.display = 'none';
		break;
		case 'registered'  :
			voyc.$('loggedinuser').innerHTML = this.uname;
			voyc.$('headeruser').style.display = 'table-cell';
			voyc.$('headerlogin').style.display = 'none';
			voyc.$('headerlogout').style.display = 'inline-block';
		break;
		case 'resetpending':
			voyc.$('loggedinuser').innerHTML = this.uname;
			voyc.$('headeruser').style.display = 'table-cell';
			voyc.$('headerlogin').style.display = 'none';
			voyc.$('headerlogout').style.display = 'inline-block';
		break;
		case 'verified'    :
			voyc.$('loggedinuser').innerHTML = this.uname;
			voyc.$('headeruser').style.display = 'table-cell';
			voyc.$('headerlogin').style.display = 'none';
			voyc.$('headerlogout').style.display = 'inline-block';
		break;
		case 'emailpending':
			voyc.$('loggedinuser').innerHTML = this.uname;
			voyc.$('headeruser').style.display = 'table-cell';
			voyc.$('headerlogin').style.display = 'none';
			voyc.$('headerlogout').style.display = 'inline-block';
		break;
	}
	
	// enable/disable request buttons in the header and dialogs
	var elems = document.querySelectorAll('[request]');
	var elem, svc;
	var self = this;
	for (i=0; i<elems.length; i++) {
		elem = elems[i];
		svc = elem.getAttribute('request');
		elem.disabled = !voyc.isSvcAllowed(svc);
	}
}
