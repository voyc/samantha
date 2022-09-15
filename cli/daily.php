<?php
/**
	get google drive space available
		https://developers.google.com/drive/api/v2/reference/about/get

	get dropbox drive space available
		https://www.dropbox.com/developers/documentation/http/documentation#users-get_space_usage

**/

require_once(dirname(__FILE__).'/../../config.php');
require_once(dirname(__FILE__).'/../phplib/emailer.php');

$to = 'John <john@voyc.com>';
$addressee = 'คุณจอห์น';
$polite = 'คะ';
$greeting = 'สวัสดี';
$subject = $greeting . $polite;
$salutation = $greeting . $addressee . $polite;

$response = file_get_contents('http://guru.voyc.com/svc/getwisdom.php');
$w =  substr($response,3);
$a = json_decode($w, true);
$quote = $a['q'] . "\n-- " . $a['a'];

$reviewWord = '';
$backupStatus = '';

$tsg = 100;  // 100 GB total leased from webfaction
$diskThreshhold = 80;
$fs = folderSize("/home/john/");
$fsg = round($fs / (1024 * 1024 * 1024));
$asg = $tsg - $fsg;
$fsgp = round(($fsg / $tsg) * 100);
$asgp = round(($asg / $tsg) * 100);
$diskSpace = '';
$diskSpace .= "$fsg GB used ($fsgp%) \n";
$diskSpace .= "$asg GB free ($asgp%) \n";
$diskSpace .= "$tsg GB total \n";
if ($fsg > $threshhold) {
	$diskSpace .= "Disk usage high.  Time to clean the disk. \n";
}

$linkToChat = '';

$message = '';
$message .= $salutation . "\n\n";
$message .= $quote . "\n\n";
$message .= $reviewWord . "\n\n";
$message .= $backupStatus . "\n\n";
$message .= $diskSpace . "\n\n";
$message .= $linkToChat . "\n\n";

sendMail($to, $subject, $message);

function folderSize($folder) {
	$iterator = new RecursiveIteratorIterator(
		new RecursiveDirectoryIterator($folder)
	);

	$totalSize = 0;
	foreach ($iterator as $file) {
		$totalSize += $file->getSize();
	}
	return $totalSize;
}
?>
