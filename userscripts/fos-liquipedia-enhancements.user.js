// ==UserScript==
// @name FOs Liquipedia Enhancements
// @namespace fo
// @include http://wiki.teamliquid.net/*
// @version 1
// @grant none
// ==/UserScript==
// copyright 2014, 2015 - FO-nTTaX
// script to change some things on Liquipedia to use with Greasemonkey
var currentwiki = window.location.href.split('/')[3];
var currentpage = window.location.href.replace('http://wiki.teamliquid.net/'+currentwiki+'/', '');
$('.dropdown-brand').find('a').each(function() {
	$(this).attr('href', $(this).attr('href').replace('Main_Page', currentpage));
});