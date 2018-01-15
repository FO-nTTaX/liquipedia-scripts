// ==UserScript==
// @name FOs Liquipedia Toolbar
// @namespace fo
// @include http://liquipedia.net/*
// @version 1
// @grant none
// ==/UserScript==
// copyright 2014, 2015 - FO-nTTaX
// script to display a toolbar on Liquipedia to use with Greasemonkey
var currentwiki = window.location.href.split('/')[3];
var currentpage = window.location.href.replace('http://liquipedia.net/'+currentwiki+'/', '');
var bar = '<div style="position:fixed; z-index: 1000; top: 0; height: 30px; width: 100%; background-image: linear-gradient(to bottom, #3C3C3C 0%, #222 100%);">';
bar += '<span><a href="http://liquipedia.net/'+currentwiki+'/" style="color: #cccccc; font-size: 24px; font-weight: bold; vertical-align: middle; padding: 3px;">FOs LP-Toolbar</a></span>';
bar += '<span style="float: right; margin: 2px; background-color: #cccccc; border-radius: 7px; padding: 1px 3px;">';
bar += '<a href="http://liquipedia.net/starcraft/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/starcraft.png"></a>';
bar += '<a href="http://liquipedia.net/starcraft2/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/starcraft2.png"></a>';
bar += '<a href="http://liquipedia.net/dota2/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/dota2.png"></a>';
bar += '<a href="http://liquipedia.net/hearthstone/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/hearthstone.png"></a>';
bar += '<a href="http://liquipedia.net/heroes/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/heroes.png"></a>';
bar += '<a href="http://liquipedia.net/smash/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/smash.png"></a>';
bar += '<a href="http://liquipedia.net/counterstrike/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/counterstrike.png"></a>';
bar += '<a href="http://liquipedia.net/overwatch/'+currentpage+'"><img src="http://www.teamliquid.net/staff/FOnTTaX/liquipedia/monthlylayout/gameicons/overwatch.png"></a>';
bar += '</span>';
bar += '<span style="float: right; margin: 2px; background-color: #171717; border-radius: 7px; padding: 1px 3px;">';
bar += '<form action="/'+currentwiki+'/index.php" method="get">';
bar += '<input value="Special:Search" name="title" type="hidden">';
bar += '<input value="Go" name="go" type="hidden">';
bar += '<input type="text" name="search" style="color: #171717; background-color: #ffffff; border: 1px solid #171717; border-radius: 7px 0 0 7px;">';
bar += '<button type="submit" style="color: #171717; background-color: #cccccc; border: 1px solid #171717; border-radius: 0 7px 7px 0;">Search</button></form>';
bar += '</span>';
bar += '</div>';
$('#globalWrapper').append(bar);
$('#column-one').css('margin-top', '30px');
