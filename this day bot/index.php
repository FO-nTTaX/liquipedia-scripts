<?php

/*
 * Licensed under GPL V2 or later
 * Built around the aweomse https://github.com/nischayn22/MediaWiki_Api
 */

include('lib.php');

$monthlengths = array(
	1 => 31,
	2 => 29,
	3 => 31,
	4 => 30,
	5 => 31,
	6 => 30,
	7 => 31,
	8 => 31,
	9 => 30,
	10 => 31,
	11 => 30,
	12 => 31
);
$wikis = array(
	'starcraft',
	'starcraft2',
	'dota2',
	'hearthstone',
	'heroes',
	'smash',
	'counterstrike',
	'overwatch',
	'warcraft',
	'fighters',
	'rocketleague',
	'clashroyale'
);
foreach($wikis as $wiki) {
	$o = new MediaWikiApi('http://wiki.teamliquid.net/' . $wiki);
	$o->login('Username', 'Password');
	for($i = 1; $i <= 12; $i++) {
		for($j = 1; $j <= $monthlengths[$i]; $j++) {
			echo "\n=========================================\nWiki: $wiki, Month: $i, Day: $j\n=========================================\n";
			$text = "__NOTOC__{{This day|year={{CURRENTYEAR}}|month=" . sprintf('%02d', $i) . "|day=" . sprintf('%02d', $j) . "}}\n\n<!--<h3>Trivia</h3>--><!--uncomment this heading and add trivia as bullet points-->";
			if($i == 2 && $j == 28) {
				$text .= "\n\n{{#ifeq:{{#time:L}}|1|<h2>February 29th</h2>{{Liquipedia:This day/2/29}}}}";
			}
			$o->editPage("Liquipedia:This_day/" . $i . "/" . $j, $text);
		}
	}
}

?>