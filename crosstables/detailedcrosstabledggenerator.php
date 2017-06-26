<?php
/* copyright 2014, 2017 - FO-nTTaX
*
* script to create the wikicode of the detailed crosstables */
$numberofteams = 10;
echo '&lt;includeonly&gt;&lt;table class="wikitable crosstable"&gt;&lt;!--<br>';
for ($i = 1; $i <= $numberofteams; $i++) {
	echo '--&gt;{{#if:{{{team'.$i.'|}}}|&lt;tr class="crosstable-tr"&gt;&lt;!--'."<br>";
	echo '--&gt;&lt;th&gt;{{TeamIcon/{{{team'.$i.'}}}}}&lt;/th&gt;&lt;!--'."<br>";
	for ($j = 1; $j <= $numberofteams; $j++) {
		echo '--&gt;{{#if:{{{hteam'.$j.'|}}}|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}{{{'.$i.'vs'.$j.'date|}}}|&lt;td class="crosstable-bgc-r{{{'.$i.'vs'.$j.'result|}}}-r{{{'.$i.'vs'.$j.'resultvs|}}}"&gt;\'\'\'{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}\'\'\'{{#if:{{{'.$i.'vs'.$j.'date|}}}|&lt;br&gt;{{#if:{{{'.$i.'vs'.$j.'link|}}}|[[{{{'.$i.'vs'.$j.'link}}}|{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;&lt;small&gt;&lt;small&gt;{{{'.$i.'vs'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;&lt;/abbr&gt;|&lt;small&gt;&lt;small&gt;{{{'.$i.'vs'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}]]|{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;&lt;small&gt;&lt;small&gt;{{{'.$i.'vs'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;&lt;/abbr&gt;|&lt;small&gt;&lt;small&gt;{{{'.$i.'vs'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}|&lt;small>&lt;small&gt;{{{'.$i.'vs'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
	}
	echo '--&gt;&lt;/tr&gt;}}&lt;!--'."<br>";
}
echo '--&gt;&lt;tr&gt;&lt;th&gt;&lt;/th&gt;&lt;!--<br>';
for ($i = 1; $i <= $numberofteams; $i++) {
	echo '--&gt;{{#if:{{{hteam'.$i.'|}}}|&lt;th&gt;{{TeamIcon/{{{hteam'.$i.'}}}}}&lt;/th&gt;}}&lt;!--<br>';
}
echo '--&gt;&lt;/tr&gt;&lt;!--<br>';
echo '--&gt;&lt;/table&gt;&lt;/includeonly&gt;&lt;noinclude&gt;{{documentation}}[[Category:Templates]]&lt;/noinclude&gt;';
?>
