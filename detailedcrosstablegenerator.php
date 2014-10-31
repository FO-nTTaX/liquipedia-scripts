<?php

/* copyright 2014 - FO-nTTaX
 *
 * script to create the wikicode of the detailed crosstables */

$numberofteams = 20;

echo '&lt;includeonly&gt;&lt;table class="wikitable crosstable" style="text-align:center;margin:0;line-height:14px"&gt;&lt;!--<br>';

for ($i = 1; $i <= $numberofteams; $i++) {
   echo '--&gt;{{#if:{{{team'.$i.'|}}}|&lt;tr style="height:30px"&gt;&lt;!--'."<br>";
   echo '--&gt;&lt;th&gt;{{TeamIcon/{{{team'.$i.'}}}}}&lt;/th&gt;&lt;!--'."<br>";
   for ($j = 1; $j <= $numberofteams; $j++) {
      if ($i == $j) {
         echo '--&gt;&lt;td style="background-color:#f2f2f2"&gt;&lt;/td&gt;&lt;!--'."<br>";
      }
      if ($i < $j) {
         echo '--&gt;{{#if:{{{team'.$j.'|}}}|{{#if:{{{team'.$i.'vsteam'.$j.'result|}}}{{{team'.$i.'vsteam'.$j.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{team'.$i.'vsteam'.$j.'result}}}|{{{team'.$i.'vsteam'.$j.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{team'.$i.'vsteam'.$j.'result}}}&gt;{{{team'.$i.'vsteam'.$j.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{{team'.$i.'vsteam'.$j.'result}}}-{{{team'.$i.'vsteam'.$j.'resultvs}}}\'\'\'{{#if:{{{team'.$i.'vsteam'.$j.'date|}}}|&lt;br&gt;{{#if:{{{team'.$i.'vsteam'.$j.'link|}}}|[[{{{team'.$i.'vsteam'.$j.'link}}}|{{#if:{{{team'.$i.'vsteam'.$j.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$i.'vsteam'.$j.'abbr}}}}}|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}]]|{{#if:{{{team'.$i.'vsteam'.$j.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$i.'vsteam'.$j.'abbr}}}}}|&lt;small>&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
      }
      if ($i > $j) {
         echo '--&gt;{{#ifeq:{{{doublerounded}}}|true|{{#if:{{{team'.$i.'vsteam'.$j.'result|}}}{{{team'.$i.'vsteam'.$j.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{team'.$i.'vsteam'.$j.'result}}}|{{{team'.$i.'vsteam'.$j.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{team'.$i.'vsteam'.$j.'result}}}&gt;{{{team'.$i.'vsteam'.$j.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{{team'.$i.'vsteam'.$j.'result}}}-{{{team'.$i.'vsteam'.$j.'resultvs}}}\'\'\'{{#if:{{{team'.$i.'vsteam'.$j.'date|}}}|&lt;br&gt;{{#if:{{{team'.$i.'vsteam'.$j.'link|}}}|[[{{{team'.$i.'vsteam'.$j.'link}}}|{{#if:{{{team'.$i.'vsteam'.$j.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$i.'vsteam'.$j.'abbr}}}}}|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}]]|{{#if:{{{team'.$i.'vsteam'.$j.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$i.'vsteam'.$j.'abbr}}}}}|&lt;small>&lt;small&gt;{{{team'.$i.'vsteam'.$j.'date}}}&lt;/small&gt;&lt;/small&gt;}}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}|{{#if:{{{team'.$j.'vsteam'.$i.'result|}}}{{{team'.$j.'vsteam'.$i.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{team'.$j.'vsteam'.$i.'result}}}|{{{team'.$j.'vsteam'.$i.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{team'.$j.'vsteam'.$i.'result}}}&lt;{{{team'.$j.'vsteam'.$i.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{{team'.$j.'vsteam'.$i.'resultvs}}}-{{{team'.$j.'vsteam'.$i.'result}}}\'\'\'{{#if:{{{team'.$j.'vsteam'.$i.'date|}}}|&lt;br&gt;{{#if:{{{team'.$j.'vsteam'.$i.'link|}}}|[[{{{team'.$j.'vsteam'.$i.'link}}}|{{#if:{{{team'.$j.'vsteam'.$i.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$j.'vsteam'.$i.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$j.'vsteam'.$i.'abbr}}}}}|&lt;small&gt;&lt;small&gt;{{{team'.$j.'vsteam'.$i.'date}}}&lt;/small&gt;&lt;/small&gt;}}]]|{{#if:{{{team'.$j.'vsteam'.$i.'abbr|}}}|{{Abbr|&lt;small&gt;&lt;small&gt;{{{team'.$j.'vsteam'.$i.'date}}}&lt;/small&gt;&lt;/small&gt;|{{{team'.$j.'vsteam'.$i.'abbr}}}}}|&lt;small>&lt;small&gt;{{{team'.$j.'vsteam'.$i.'date}}}&lt;/small&gt;&lt;/small&gt;}}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
      }
   }
   echo '--&gt;&lt;/tr&gt;}}&lt;!--'."<br>";
}
echo '--&gt;&lt;tr&gt;&lt;th&gt;&lt;/th&gt;&lt;!--<br>';
for ($i = 1; $i <= $numberofteams; $i++) {
   echo '--&gt;{{#if:{{{team'.$i.'|}}}|&lt;th&gt;{{TeamIcon/{{{team'.$i.'}}}}}&lt;/th&gt;}}&lt;!--<br>';
}
echo '--&gt;&lt;/tr&gt;&lt;!--<br>';
echo '--&gt;&lt;/table&gt;&lt;/includeonly&gt;';

?>
