<?php

/* copyright 2014 - FO-nTTaX
 *
 * script to create the wikicode of the crosstables */

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
         echo '--&gt;{{#if:{{{team'.$j.'|}}}|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{'.$i.'vs'.$j.'result}}}|{{{'.$i.'vs'.$j.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{'.$i.'vs'.$j.'result}}}&gt;{{{'.$i.'vs'.$j.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{#if:{{{'.$i.'vs'.$j.'link|}}}|[[{{{'.$i.'vs'.$j.'link}}}|&lt;span style="margin:0;width:100%;height:100%;display:block"&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/span&gt;]]|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
      }
      if ($i > $j) {
         echo '--&gt;{{#ifeq:{{{doublerounded}}}|true|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{'.$i.'vs'.$j.'result}}}|{{{'.$i.'vs'.$j.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{'.$i.'vs'.$j.'result}}}&gt;{{{'.$i.'vs'.$j.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{#if:{{{'.$i.'vs'.$j.'link|}}}|[[{{{'.$i.'vs'.$j.'link}}}|&lt;span style="margin:0;width:100%;height:100%;display:block"&gt;{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}&lt;/span&gt;]]|{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}|{{#if:{{{'.$j.'vs'.$i.'result|}}}{{{'.$j.'vs'.$i.'resultvs|}}}|&lt;td style="padding:0;background-color:#{{#ifeq:{{{'.$j.'vs'.$i.'result}}}|{{{'.$j.'vs'.$i.'resultvs}}}|ffffff|{{#ifeq:{{#expr:{{{'.$j.'vs'.$i.'result}}}&lt;{{{'.$j.'vs'.$i.'resultvs}}}}}|1|ccffcc|ffcccc}}}}"&gt;\'\'\'{{#if:{{{'.$j.'vs'.$i.'link|}}}|[[{{{'.$j.'vs'.$i.'link}}}|&lt;span style="margin:0;width:100%;height:100%;display:block"&gt;{{{'.$j.'vs'.$i.'resultvs}}}-{{{'.$j.'vs'.$i.'result}}}&lt;/span&gt;]]|{{{'.$j.'vs'.$i.'resultvs}}-{{{'.$j.'vs'.$i.'result}}}}}\'\'\'&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
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
