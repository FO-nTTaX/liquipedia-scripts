<?php

/* copyright 2014 - FO-nTTaX
 *
 * script to create an example crosstable content */

for ($i = 1; $i <= 20; $i++) {
    echo '&lt;!--Games of Team '.$i.'--&gt;<br>';
    for ($j = 1; $j <= 20; $j++) {
        if ($i != $j) {
            $rand1 = rand (0,6);
            $rand2 = rand (0,6);
            echo '|'.$i.'vs'.$j.'result='.$rand1.'|'.$i.'vs'.$j.'resultvs='.$rand2.'|'.$i.'vs'.$j.'link=Main_Page<br>';
        }
    }
}

?>
