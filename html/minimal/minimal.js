/** 
	class Minimal
	@constructor
*/
voyc.Minimal = function() {
	// is singleton
	if (voyc.Minimal._instance) return voyc.Minimal._instance;
	else voyc.Minimal._instance = this;

	this.theme = '';
	this.popup = null;
	this.dropcb = null;
}

voyc.Minimal.prototype = {
	/**
		@param {Element|null} [e=null]
	*/
	attachAll: function(e) {
		this.fixInitiallyHidden(e);
		this.fixFixedHeader(e);
		this.attachShowHide(e);
		this.attachExpanders(e);
		this.attachOpenClose(e);
		this.attachToggleButtons(e);
		this.attachCssButtons(e);
		this.attachFixHeaderButtons(e);
		this.attachSelect(e);
		this.attachDnd(e);
	},

	fixInitiallyHidden: function(element) {
		var elem = element || document;
		var elems = elem.querySelectorAll('[initially]');
		for (var i=0; i<elems.length; i++) {
			elems[i].removeAttribute('initially');
			elems[i].removeAttribute('hidden');
		}
	},

	fixFixedHeader: function(element) {
		var elem = element || document;

		// find header element
		var header = elem.querySelector('header');
		var isFixed = header && header.classList.contains('fixed');
		var ht = (header) ? header.offsetHeight : 0;
		var fht = (isFixed) ? ht : 0;
		
		// fix padding-top of the scrolling element, the next sibling after the fixed header
		var fscroller = elem.querySelector('header + *');
		if (fscroller) {
			fscroller.style.paddingTop = fht + 'px';
		}

		// likewise fix padding-top of all anchor navlabels in the scrolling element
		var elems = elem.querySelectorAll('.navlabel');
		for (var i=0; i<elems.length; i++) {
			elems[i].style.paddingTop = fht + 'px';
		}

		// fix top of all popup dialogs positioned just under the header
		elems = elem.querySelectorAll('.dropdown.fromheader, .leftnav.fromheader');
		for (var i=0; i<elems.length; i++) {
			elems[i].style.top = ht + 'px';
		}

		// toggle class of fixheader buttons
		var fixbtns = elem.querySelectorAll('[fixheader]');
		for (var d,i=0; i<fixbtns.length; i++) {
			d = fixbtns[i];
			if (isFixed) {
				d.classList.add('down');
			}
			else {
				d.classList.remove('down');
			}
		}
	},

	show: function(eid) {
		var e = voyc.$(eid);
		e.removeAttribute('hidden');
	},

	hide: function(eid) {
		var e = voyc.$(eid);
		e.setAttribute('hidden', '');
	},

	attachShowHide: function(element) {
		var elem = element || document;
		var elems = elem.querySelectorAll('[show]');
		var self = this;
		for (var i=0; i<elems.length; i++) {
			elems[i].addEventListener('click', function(event) {
				var eid = event.currentTarget.getAttribute('show');
				self.show(eid);
			}, false);
		}
		elems = elem.querySelectorAll('[hide]');
		for (var i=0; i<elems.length; i++) {
			elems[i].addEventListener('click', function(event) {
				var eid = event.currentTarget.getAttribute('hide');
				self.hide(eid);
			}, false);
		}
	},

	attachExpanders: function(element) {
		var elem = element || document;
		var elems = elem.querySelectorAll('[expand]');
		for (var i=0; i<elems.length; i++) {
			elems[i].classList.add('expander');
			elems[i].classList.add('collapsed');
			var f = elems[i].getAttribute('expand');
			voyc.$(f).classList.add('expandable');
			voyc.$(f).classList.add('collapsed');
			var self = this;
			elems[i].addEventListener('click', function(event) {
				var e = event.currentTarget;
				var f = e.getAttribute('expand');
				var t = voyc.$(f);
				var b = (t.classList.contains('collapsed'));
				if (b) {
					self.expand(e,t);
				}
				else {
					self.collapse(e,t);
				}
			}, false);
		}
	},

	expand: function(e,t) {
		e.classList.remove('collapsed');
		t.removeAttribute('hidden')
		var el = t;  // closure variable
		setTimeout(function() {
			el.classList.remove('collapsed');
		},1);
		setTimeout(function() {
			el.classList.remove('collapsed');
		},300);
	},

	collapse: function(e,t) {
		e.classList.add('collapsed');
		t.classList.add('collapsed');
		var el = t;  // closure variable
		setTimeout(function() {
			el.setAttribute('hidden','')
		},200);
	},
	
	attachOpenClose: function(element) {
		var doc = element || document;
		var elems = doc.querySelectorAll('[open]');
		var self = this;
		for (var i=0; i<elems.length; i++) {
			elems[i].addEventListener('click', function(event) {
				var eid = event.currentTarget.getAttribute('open');
				self.openPopup(eid);
			}, false);
		}
		elems = doc.querySelectorAll('[close]');
		for (var i=0; i<elems.length; i++) {
			elems[i].addEventListener('click', function(event) {
				self.closePopup();
			}, false);
		}
		window.addEventListener('keyup', function(event) {
			if (event.keyCode == 27) {  // escape key
				self.closePopup();
			}
		}, false);
	},

	attachToggleButtons: function(element) {
		var elem = element || document;
		var togglebtns = elem.querySelectorAll('[toggle]');
		for (var d,i=0; i<togglebtns.length; i++) {
			d = togglebtns[i];
			d.addEventListener('click', function(event) {
				var t = event.currentTarget;
				if (t.classList.contains('down')) {
					t.classList.remove('down');
				}
				else {
					// push this one down
					t.classList.add('down');

					// pull all the others up
					var name = t.getAttribute('toggle');
					if (name) {
						var btns = document.querySelectorAll('[toggle='+name+']');
						for (var i=0; i<btns.length; i++) {
							if (btns[i] != t) {
								btns[i].classList.remove('down');
							}
						}
					}
				}
				t.blur();
			}, false);

			// remove whitespace from between a group of toggle buttons
			var name = d.getAttribute('toggle');
			if (name) {
				voyc.removeWhiteSpace( d.parentElement);
			}
		}
	},

	attachCssButtons: function(element) {
		var elem = element || document;
		this.path = (window.location.pathname.indexOf('minimal') > -1 || window.location.hostname.indexOf('minimal') > -1) ? '' : 'minimal/';
		this.path += 'theme/';
		var cssbtns = elem.querySelectorAll('[css]');
		for (var d,i=0; i<cssbtns.length; i++) {
			d = cssbtns[i];
			var self = this;
			d.addEventListener('click', function(event) {
				var name = event.currentTarget.getAttribute('css');
				var isLoading = !(name == self.theme);
				if (isLoading) {
					if (self.theme) {
						voyc.unloadCss(self.path + self.theme + '.css');
					}
					self.theme = name;
					voyc.loadCss(self.path + self.theme + '.css');
				}
				else {
					voyc.unloadCss(self.path + self.theme + '.css');
					self.theme = '';
				}
				// self.fixFixedHeader(); needs to happen after css successfully loaded or unloaded
			}, false);
		}
	},

	attachFixHeaderButtons: function(element) {
		var elem = element || document;
		var header = elem.querySelector('header');
		var isFixed = header && header.classList.contains('fixed');
		var fixbtns = elem.querySelectorAll('[fixheader]');
		for (var d,i=0; i<fixbtns.length; i++) {
			d = fixbtns[i];
			if (isFixed) {
				d.classList.add('down');
			}
			var self = this;
			d.addEventListener('click', function(event) {
				var header = elem.querySelector('header');
				if (header) {
					header.classList.toggle('fixed');
					self.fixFixedHeader(elem);
				}
			}, false);
		}
	},

	attachSelect: function(element) {
		var elem = element || document;
		// click the header to select all rows
		var a = elem.querySelectorAll('[select] h3');
		for (var i=0; i<a.length; i++) {
			a[i].addEventListener('click', function(e) {
				var a = e.currentTarget.parentElement.querySelectorAll('tr');
				for (var i=0; i<a.length; i++) {
					a[i].classList.toggle('selected');
				}
			}, false);
			a[i].addEventListener('mousedown', function(e) {
				e.preventDefault(); // prevent text selection
			}, false);
		}

		// select each row individually
		a = elem.querySelectorAll('[select] table tbody tr');
		for (var i=0; i<a.length; i++) {
			a[i].addEventListener('click', function(e) {
				e.currentTarget.classList.toggle('selected');
			}, false);
			a[i].addEventListener('mousedown', function(e) {
				e.preventDefault(); // prevent text selection
			}, false);
		}
	},
				
	attachDnd: function(element, ondropcb) {
		var elem = element || document;

		if (!this.dragger) {
			this.dragger = new voyc.Dragger();
		}

		var drags = elem.querySelectorAll('[drag]');
		for (var i=0; i<drags.length; i++) {
			this.dragger.enableDrag(drags[i]);
		}

		var drops = elem.querySelectorAll('[drop]');
		for (var i=0; i<drops.length; i++) {
			// if there is a child ul, enable the ul, otherwise enable the element itself
			var subdrops = drops[i].querySelectorAll('ul,table');
			if (subdrops.length > 0) {
				for (var j=0; j<subdrops.length; j++) {
					this.dragger.enableDrop(subdrops[j]);
				}
			}
			else {
				this.dragger.enableDrop(drops[i]);
			}
		}

		var lists = elem.querySelectorAll('[draglist]');
		for (var i=0; i<lists.length; i++) {
			drags = lists[i].querySelectorAll('li,tr');
			for (var j=0; j<drags.length; j++) {
				this.dragger.enableDrag(drags[j]);
				drags[j].setAttribute('drag', '');
			}
		}

		lists = elem.querySelectorAll('[droplist] ul');
		for (var i=0; i<lists.length; i++) {
			drops = lists[i].querySelectorAll('li');
			if (drops.length) {
				for (var lx,j=0; j<=drops.length; j++) {
					lx = document.createElement(drops[0].tagName);
					lx.setAttribute('drop', '');
					lists[i].insertBefore(lx, drops[j]);
					this.dragger.enableDrop(lx);
				}
			}
			else {
				var lx = document.createElement('li');
				lx.setAttribute('drop', '');
				lists[i].appendChild(lx);
				this.dragger.enableDrop(lx);
			}
		}

		lists = elem.querySelectorAll('table[droplist] tbody');
		for (var i=0; i<lists.length; i++) {
			drops = lists[i].querySelectorAll('tr');
			var nCols = drops[0].childNodes.length;
			for (var lx,j=0; j<=drops.length; j++) {
				lx = document.createElement(drops[0].tagName);
				tx = document.createElement('td');
				tx.setAttribute('colspan', nCols);
				lx.appendChild(tx);
				lx.setAttribute('drop', '');
				lists[i].insertBefore(lx, drops[j]);
				this.dragger.enableDrop(lx);
			}
		}

		// this supports only one client ondrop handler
		if (ondropcb) {
			this.dropcb = ondropcb;
		}
		this.dragger.addListener(null, 'drop', function(e,x,y,t) {
			if (t.tagName.toLowerCase() == 'li' || t.tagName.toLowerCase() == 'tr') {
				t.parentElement.insertBefore(e,t);
			}
			else {
				t.appendChild(e);
			}
			(new voyc.Minimal()).dropcb(e,x,y,t);
		});
	},
	
	wait: function() {
		this.show('wait');
	},
	
	killWait: function() {
		if (voyc.$('wait')) {
			this.hide('wait');
		}
	},

	closePopup: function() {
		this.killWait();
		if (this.popup) {
			if (this.popup.hasAttribute('modal')) {
				this.popup.reset();
				voyc.$('dialog-msg').innerHTML = '';
				voyc.$('modalcontainer').setAttribute('hidden','')
				voyc.$('offscreen').appendChild(this.popup);
			}
			else {
				this.popup.classList.remove('open');
				window.removeEventListener('click', voyc.clickAnywhereToClose, false);
			}
			this.popup = null;
		}
	},

	openPopup: function(eid) {
		var prev = this.popup;
		if (this.popup) {
			this.closePopup();
		}
		if (!prev || prev.id != eid) {
			if (voyc.$(eid).hasAttribute('modal')) {
				voyc.$('modalcontainer').removeAttribute('hidden');
				voyc.$('dialog').appendChild(voyc.$(eid));
				voyc.$('modaltitle').innerHTML = voyc.$(eid).getAttribute('title')
			}
			else {
				voyc.$(eid).classList.add('open');
				setTimeout(function() {
					window.addEventListener('click', voyc.clickAnywhereToClose, false);
				}, 25);
			}
			this.popup = voyc.$(eid);
			voyc.$(eid).dispatchEvent(new Event('open'))
		}
	},
}

/* 
	global function
*/
voyc.clickAnywhereToClose = function(event) {
	var isInPopup = false;
	var e = event.target;
	while (e) {
		if (e.classList && e.classList.contains('popup') && e.classList.contains('open')) {
			isInPopup = true;
			break;
		}
		e = e.parentElement;
	}

	if (!isInPopup) {
		var m = new voyc.Minimal();
		m.closePopup();
	}
}

voyc.show = function(eid) {
	(new voyc.Minimal).show(eid);
}
voyc.hide = function(eid) {
	(new voyc.Minimal).hide(eid);
}
voyc.openPopup = function(eid) {
	(new voyc.Minimal).openPopup(eid);
}
voyc.closePopup = function() {
	(new voyc.Minimal).closePopup();
}
voyc.wait = function() {
	(new voyc.Minimal).wait();
}
voyc.killWait = function() {
	(new voyc.Minimal).killWait();
}

/* 
	DOM event handler
*/
window.addEventListener('load', function() {
	var minimal = new voyc.Minimal();
	minimal.attachAll();
}, false);
