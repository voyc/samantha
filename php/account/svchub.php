<?php
/**
	user authentication svc entry point
**/
if (file_exists(dirname(__FILE__).'/../config.php')) {
	require_once(dirname(__FILE__).'/../config.php');  // native
}
else {
	require_once(dirname(__FILE__).'/../../../config.php');  // super
}
require_once('lib/str.php');
require_once('lib/db.php');
require_once('lib/validate.php');
require_once('lib/crypto.php');
require_once('lib/cors.php');
require_once('lib/log.php');

writeHeader();

/* 
	this function is not yet implemented or tested
	todo:
		implement html/svc.php
		change all svc calls
*/
$supported_svcs = array(
	'register'       ,
	'verify' ,
	'forgotpassword' ,
	'resetpassword'  ,
	'login'          ,
	'relogin'        ,
	'logout'         ,
	'changepassword' ,
	'changeusername' ,
	'changeemail'    ,
	'verifyemail'
);
		
function validateSvc($taint) {
	global $supported_svcs;
	$clean = in_array($taint, $supported_svcs) ? $taint : 0;
	return $clean;
}

function svchub() {
	// get the svc name
	$taint_svc = isset($_POST['svc']) ? $_POST['svc'] : 0;

	// validate the svc name
	$svc = validateSvc($taint_svc);
	if (!$svc) {
		Log::open("unsupported svc: $svc.$taint_svc");
		return;
	}

	$includefile = $svc . '.php';
	
	Log::open($svc);
	require_once($includefile);
	$a = $svc();
	echo json_encode($a);
	Log::close($a['status']);
	return;
}
?>
