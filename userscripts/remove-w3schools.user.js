// ==UserScript==
// @name        Remove w3schools from google results
// @namespace   fo
// @include     https://www.google.*
// @version     1
// @grant       none
// ==/UserScript==
window.addEventListener("load", function() {
	window.setTimeout(function() {
		var google_results = document.querySelectorAll('div.g');
		for(var google_result of google_results) {
			var fucking_w3school_results = google_result.querySelectorAll('cite._Rm');
			for(var fucking_w3school_result of fucking_w3school_results) {
				if(fucking_w3school_result.innerHTML.startsWith('www.w3schools.com')) {
					google_result.style.display = "none";
				}
			}
		}
	}, 1000);
});