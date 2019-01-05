<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=300px, initial-scale=1">
<link href="bootstrap.css" rel="stylesheet">
<link href="bootstrap-switch.css" rel="stylesheet">
<script src="jquery.js"></script>
<script src="bootstrap-switch.js"></script>

</head>
<body>
	<p align="center">
<?php
$page=$_SERVER['PHP_SELF'];
header("Refresh: 1; url=$page");
$output=shell_exec("sudo python /home/pi/getTempandHum.py");
echo "Current Readings are <br> $output";

?>
</p>
</body>
</html>
