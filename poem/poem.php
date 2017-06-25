<?php
if ($argc > 1) {
	$filename = $argv[1];
} else { die("No filename given"); }
$fh = fopen($filename, "r");

$title = rtrim(fgets($fh));
$by = rtrim(fgets($fh));

$maxlen = 0;
$lines = array();
while($line = fgets($fh)) {
	$line = rtrim($line);
	if ($line == "---") {
		break;
	}
	array_push($lines, $line);

	$curlen = strlen($line);
	if ($curlen > $maxlen) {
		$maxlen = $curlen;
	}
}
?>
<!DOCTYPE html>
<html>
<head>
 <meta charset="UTF-8" />
 <title><?php echo "$title by $by"; ?></title>
 <link rel="stylesheet" type="text/css" href="/css/poem.css"
</head>
<body>
 <div class="wrapper" style="width:<?php echo $maxlen; ?>ch">
 <h1><?php echo $title; ?></h1>
 <section class="poem">
<?php 
foreach ($lines as $line) {
	echo "$line\n";
}
?>
 <div class="by">-- <?php echo $by; ?></div>
</section>
<?php
while ($line = fgets($fh)) {
	echo $line;
}
?>
</body>
