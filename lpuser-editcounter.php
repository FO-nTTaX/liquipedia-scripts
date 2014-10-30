<?php

/* script to query ones editcounts from the wikis via the api */

if (isset($_GET['name'])) {$name=$_GET['name'];} else {$name ='FO-nTTaX';}
echo '<!DOCTYPE html><html><head><title>FOs Liquipedia Editcounter</title></head><body>';
$wikis = array('starcraft', 'starcraft2', 'dota2', 'hearthstone', 'heroes', 'smash');
foreach($wikis as $id => $wiki) {
	$inarr[$id] = unserialize(file_get_contents('http://wiki.teamliquid.net/'.$wiki.'/api.php?action=query&format=php&list=users&ususers='.$name.'&usprop=editcount'));
	$count[$id] = $inarr[$id]['query']['users'][0]['editcount'];
}
echo '<table>';
foreach ($wikis as $id => $wiki) {
	echo '<tr><td>'.$wiki.'</td><td>'.$count[$id].'</td></tr>';
}
echo '<tr><td>sum</td><td>'.array_sum($count).'</td></tr>';
echo '</table></body></html>';
?>
