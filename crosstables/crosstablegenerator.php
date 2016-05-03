<?php

/* copyright 2014, 2015 - FO-nTTaX
 *
 * script to create the wikicode of the crosstables */

$numberofteams = 20;

echo '&lt;includeonly&gt;&lt;table class="wikitable crosstable"&gt;&lt;!--<br>';

for ($i = 1; $i <= $numberofteams; $i++) {
	echo '--&gt;{{#if:{{{team'.$i.'|}}}|&lt;tr class="crosstable-tr"&gt;&lt;!--'."<br>";
	echo '--&gt;&lt;th&gt;{{#ifeq:{{{team'.$i.'dota|}}}|true|{{TeamIcon/dota|{{{team'.$i.'}}}}}|{{TeamIcon/{{{team'.$i.'}}}}}}}&lt;/th&gt;&lt;!--'."<br>";
	for ($j = 1; $j <= $numberofteams; $j++) {
		if ($i == $j) {
			echo '--&gt;&lt;td class="crosstable-bgc-cross"&gt;&lt;/td&gt;&lt;!--'."<br>";
		}
		if ($i < $j) {
			echo '--&gt;{{#if:{{{team'.$j.'|}}}|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$i.'vs'.$j.'result|}}}-r{{{'.$i.'vs'.$j.'resultvs|}}}"&gt;\'\'\'{{#if:{{{'.$i.'vs'.$j.'link|}}}|[[{{{'.$i.'vs'.$j.'link}}}|&lt;span class="crosstable-bgc-span"&gt;{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/abbr&gt;|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}&lt;/span&gt;]]|{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/abbr&gt;|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
		}
		if ($i > $j) {
			echo '--&gt;{{#ifeq:{{{doublerounded}}}|true|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$i.'vs'.$j.'result|}}}-r{{{'.$i.'vs'.$j.'resultvs|}}}"&gt;\'\'\'{{#if:{{{'.$i.'vs'.$j.'link|}}}|[[{{{'.$i.'vs'.$j.'link}}}|&lt;span class="crosstable-bgc-span"&gt;{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/abbr&gt;|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}&lt;/span&gt;]]|{{#if:{{{'.$i.'vs'.$j.'abbr|}}}|&lt;abbr title=&quot;{{{'.$i.'vs'.$j.'abbr}}}&quot;&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/abbr&gt;|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}|{{#if:{{{'.$j.'vs'.$i.'result|}}}{{{'.$j.'vs'.$i.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$j.'vs'.$i.'result|}}}-r{{{'.$j.'vs'.$i.'resultvs|}}}"&gt;\'\'\'{{#if:{{{'.$j.'vs'.$i.'link|}}}|[[{{{'.$j.'vs'.$i.'link}}}|&lt;span class="crosstable-bgc-span"&gt;{{#if:{{{'.$j.'vs'.$i.'abbr|}}}|&lt;abbr title=&quot;{{{'.$j.'vs'.$i.'abbr}}}&quot;&gt;{{{'.$j.'vs'.$i.'result}}}-{{{'.$j.'vs'.$i.'resultvs}}}&lt;/abbr&gt;|{{{'.$j.'vs'.$i.'result}}}-{{{'.$j.'vs'.$i.'resultvs}}}}}&lt;/span&gt;]]|{{#if:{{{'.$j.'vs'.$i.'abbr|}}}|&lt;abbr title=&quot;{{{'.$j.'vs'.$i.'abbr}}}&quot;&gt;{{{'.$j.'vs'.$i.'resultvs}}}-{{{'.$j.'vs'.$i.'result}}}&lt;/abbr&gt;|{{{'.$j.'vs'.$i.'resultvs}}}-{{{'.$j.'vs'.$i.'result}}}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
		}
	}
	echo '--&gt;&lt;/tr&gt;}}&lt;!--'."<br>";
}
echo '--&gt;&lt;tr&gt;&lt;th&gt;&lt;/th&gt;&lt;!--<br>';
for ($i = 1; $i <= $numberofteams; $i++) {
	echo '--&gt;{{#if:{{{team'.$i.'|}}}|&lt;th&gt;{{#ifeq:{{{team'.$i.'dota|}}}|true|{{TeamIcon/dota|{{{team'.$i.'}}}}}|{{TeamIcon/{{{team'.$i.'}}}}}}}&lt;/th&gt;}}&lt;!--<br>';
}
echo '--&gt;&lt;/tr&gt;&lt;!--<br>';
echo '--&gt;&lt;/table&gt;&lt;/includeonly&gt;&lt;noinclude&gt;{{documentation}}[[Category:Templates]]&lt;/noinclude&gt;';

?>
