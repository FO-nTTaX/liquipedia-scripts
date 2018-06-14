// ==UserScript==
// @name        No more hover dropdown on LP
// @namespace   FileFace
// @include     https://liquipedia.net/*
// @version     1
// @grant       none
// ==/UserScript==
$(document).ready(function(){
	$('.dropdown, .dropdown-toggle').each(function(){
		$(this).unbind('mouseover mouseout mouseenter mouseleave');
	});
});