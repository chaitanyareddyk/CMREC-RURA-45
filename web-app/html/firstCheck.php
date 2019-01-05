<?php 

exec("sudo python /home/pi/firstCheck.py " ,$output);

echo json_encode($output); 
