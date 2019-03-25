<?php

require_once "Mail.php";  // pear, for smtp method

$email_method = 'smtp';

function sendMail($to, $subject, $message) {
	global $email_method;
	$snow = date('Y-m-d h:i:s A', time());
	$message = $message . "\n" . $snow . "\n";
	if ($email_method == 'smtp') {
		$headers = array (
			"From" => Config::$email_from,
			"To" => $to,
			"Subject" => $subject
		);
		$smtp = Mail::factory("smtp", array (
			'host' => Config::$email_server,
			'auth' => true,
			'username' => Config::$email_user,
			'password' => Config::$email_password
		));
		$r = $smtp->send($to, $headers, $message);
		if ($r <> 1) {
			print $r + "\n";
		}
	}
	else { // ($email_method == 'web')
		$additional_headers = '';
		$additional_headers .= 'From: ' . Config::$email_from . "\r\n";
		$additional_headers .= 'Reply-To: ' . Config::$email_from . "\r\n";
		$additional_parameters = '';
		$r = mail($to, $subject, $message, $additional_headers, $additional_parameters);
		if (!$r) {
			print $r + "\n";
		}
	}
}
?>
