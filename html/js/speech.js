/**
	class Speech
	wraps javascript utterance object for text-to-speech
	public methods:
		speak()
		listen()
**/
voyc.Speech = function() {
	this.utterance = new SpeechSynthesisUtterance('')
	this.rate = 1; // 0.1 to 10, default 1
	this.pitch = 1; // 0 to 2, default 1
	this.volume = 1; // 0 to 1, default 1  
	this.langEng = 'en-US';
	this.langThai = 'th-TH';
	this.lang = this.langEng; // BCP 47 language tag
	this.voices = []; // see lab.hagstrand.com/speech/speechSynth.html
	this.text = 'hello';
}
	
voyc.Speech.prototype.speak = function(text,lang,rate,speaker) {
	var text = text || this.text; 
	var gen = (speaker) ? speaker.gender : 'f';  // m or f
	var lang = (lang) ? lang : 'e'; // e or t
	var rate = rate || this.rate;

	this.utterance.text = text;
	this.utterance.pitch = (gen == 'f') ? this.pitch : this.pitch/2;
	this.utterance.volume = this.volume;
	this.utterance.rate = rate;
	this.utterance.lang = (lang == 't') ? this.langThai : this.langEng;
	//utterance.voice = voices[0];
	speechSynthesis.speak(this.utterance)
}
