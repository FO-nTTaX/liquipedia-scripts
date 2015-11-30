<?php

/* copyright 2014, 2015 - FO-nTTaX
 *
 * script to create the wikicode of the player crosstables */

$numberofteams = 10;

echo '&lt;includeonly&gt;&lt;table class="wikitable crosstable"&gt;&lt;!--<br>';
echo '--&gt;{{#ifeq:{{{displaystats}}}|true|&lt;tr class="crosstable-tr"&gt;&lt;th colspan="{{#expr:1';
for ($i = 1; $i <= $numberofteams; $i++) {
   echo '{{#if:{{{player'.$i.'|}}}|+1}}';
}
echo '}}"&gt;Crosstable&lt;/th&gt;&lt;th&gt;Group Record&lt;/th&gt;&lt;/tr&gt;}}&lt;!--'."<br>";

for ($i = 1; $i <= $numberofteams; $i++) {
   echo '--&gt;{{#if:{{{player'.$i.'|}}}|&lt;tr class="crosstable-tr"&gt;&lt;!--'."<br>";
   echo '--&gt;&lt;th style="min-width:{{{cell-width|100}}}px;"&gt;{{player|{{{player'.$i.'}}}|char={{{player'.$i.'char|}}}|flag={{{player'.$i.'flag|}}}|link={{{player'.$i.'link|}}}}}&lt;/th&gt;&lt;!--'."<br>";
   for ($j = 1; $j <= $numberofteams + 1; $j++) {
      if ($i == $j) {
         echo '--&gt;&lt;td class="crosstable-bgc-cross"&gt;&lt;/td&gt;&lt;!--'."<br>";
      } elseif ($j == $numberofteams + 1) {
         echo '--&gt;{{#ifeq:{{{displaystats}}}|true|&lt;td style="background-color:{{#switch: {{{player'.$i.'bg}}}|proceed|up = <nowiki>#cfc</nowiki>|stayup = <nowiki>#efa</nowiki>|stay = <nowiki>#ff9</nowiki>|staydown = <nowiki>#fda</nowiki>|drop|down = <nowiki>#fcc</nowiki>|#f9f9f9}};"&gt;\'\'\'{{#if:{{{player'.$i.'_w|}}}{{{player'.$i.'_l|}}}|{{{player'.$i.'_w|0}}}-{{{player'.$i.'_l|0}}}|{{#expr:0';
         for ($k = 1; $k <= $numberofteams; $k++) {
            if ($i < $k) {
               echo '+{{#ifexpr:{{{'.$i.'vs'.$k.'result|0}}}&gt;{{{'.$i.'vs'.$k.'resultvs|0}}}|1|0}}{{#ifeq:{{{doublerounded}}}|true|+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&lt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}}}';
            } elseif ($i > $k) {
               echo '{{#ifeq:{{{doublerounded}}}|true|+{{#ifexpr:{{{'.$i.'vs'.$k.'result|0}}}&gt;{{{'.$i.'vs'.$k.'resultvs|0}}}|1|0}}+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&lt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}|+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&lt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}}}';
            }
         }
         echo '}}-{{#expr:0';
         for ($k = 1; $k <= $numberofteams; $k++) {
            if ($i < $k) {
               echo '+{{#ifexpr:{{{'.$i.'vs'.$k.'result|0}}}&lt;{{{'.$i.'vs'.$k.'resultvs|0}}}|1|0}}{{#ifeq:{{{doublerounded}}}|true|+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&gt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}}}';
            } elseif ($i > $k) {
               echo '{{#ifeq:{{{doublerounded}}}|true|+{{#ifexpr:{{{'.$i.'vs'.$k.'result|0}}}&lt;{{{'.$i.'vs'.$k.'resultvs|0}}}|1|0}}+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&gt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}|+{{#ifexpr:{{{'.$k.'vs'.$i.'result|0}}}&gt;{{{'.$k.'vs'.$i.'resultvs|0}}}|1|0}}}}';
            }
         }
         echo '}}}}\'\'\'&lt;/td&gt;}}&lt;!--'."<br>";
      } elseif ($i < $j) {
         echo '--&gt;{{#if:{{{player'.$j.'|}}}|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$i.'vs'.$j.'result|}}}-r{{{'.$i.'vs'.$j.'resultvs|}}} bracket-game"&gt;&lt;div&gt;\'\'\'{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}\'\'\'&lt;/div&gt;{{#if:{{{'.$i.'vs'.$j.'details|}}}|{{BracketMatchPlayers|{{#expr:5+{{{cell-width|100}}}}}|{{#if:{{{player'.$i.'|}}}|{{{player'.$i.'}}}|TBD}}|{{#if:{{{player'.$j.'|}}}|{{{player'.$j.'}}}|TBD}}}} {{{'.$i.'vs'.$j.'details}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
      } elseif ($i > $j) {
         echo '--&gt;{{#ifeq:{{{doublerounded}}}|true|{{#if:{{{'.$i.'vs'.$j.'result|}}}{{{'.$i.'vs'.$j.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$i.'vs'.$j.'result|}}}-r{{{'.$i.'vs'.$j.'resultvs|}}} bracket-game"&gt;&lt;div&gt;\'\'\'{{{'.$i.'vs'.$j.'result}}}-{{{'.$i.'vs'.$j.'resultvs}}}\'\'\'&lt;/div&gt;{{#if:{{{'.$i.'vs'.$j.'details|}}}|{{BracketMatchPlayers|{{#expr:5+{{{cell-width|100}}}}}|{{#if:{{{player'.$i.'|}}}|{{{player'.$i.'}}}|TBD}}|{{#if:{{{player'.$j.'|}}}|{{{player'.$j.'}}}|TBD}}}} {{{'.$i.'vs'.$j.'details}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}|{{#if:{{{'.$j.'vs'.$i.'result|}}}{{{'.$j.'vs'.$i.'resultvs|}}}|&lt;td class="crosstable-bgc-r{{{'.$j.'vs'.$i.'resultvs|}}}-r{{{'.$j.'vs'.$i.'result|}}} bracket-game"&gt;&lt;div&gt;\'\'\'{{{'.$j.'vs'.$i.'resultvs}}}-{{{'.$j.'vs'.$i.'result}}}\'\'\'&lt;/div&gt;{{#if:{{{'.$j.'vs'.$i.'details|}}}|{{BracketMatchPlayers|{{#expr:5+{{{cell-width|100}}}}}|{{#if:{{{player'.$j.'|}}}|{{{player'.$j.'}}}|TBD}}|{{#if:{{{player'.$i.'|}}}|{{{player'.$i.'}}}|TBD}}}} {{{'.$j.'vs'.$i.'details}}}}}&lt;/td&gt;|&lt;td&gt;&lt;/td&gt;}}}}&lt;!--<br>';
      }
   }
   echo '--&gt;&lt;/tr&gt;}}&lt;!--'."<br>";
}
echo '--&gt;&lt;tr&gt;&lt;th&gt;&lt;/th&gt;&lt;!--<br>';
for ($i = 1; $i <= $numberofteams; $i++) {
   echo '--&gt;{{#if:{{{player'.$i.'|}}}|&lt;th style="min-width:{{{cell-width|100}}}px;"&gt;{{player|{{{player'.$i.'}}}|char={{{player'.$i.'char|}}}|flag={{{player'.$i.'flag|}}}|link={{{player'.$i.'link|}}}}}&lt;/th&gt;}}&lt;!--<br>';
}
echo '--&gt;{{#ifeq:{{{displaystats}}}|true|&lt;th style="min-width:{{{cell-width|100}}}px;"&gt;&lt;/th&gt;}}&lt;!--<br>';
echo '--&gt;&lt;/tr&gt;&lt;!--<br>';
echo '--&gt;&lt;/table&gt;&lt;/includeonly&gt;&lt;noinclude&gt;{{documentation}}[[Category:Templates]]&lt;/noinclude&gt;';

?>
