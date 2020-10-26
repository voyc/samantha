<?php
/**
	svc forgotpassword
	Request a new password.
*/
function forgotpassword() {
	$a = array(
		'status' => 'system-error'
	);

	// get raw inputs
	$taint_both = isset($_POST['both']) ? $_POST['both'] : 0;

	// validate inputs
	$both = validateBoth($taint_both);

	// validate parameter set
	if (!$both){
		Log::write(LOG_WARNING, 'attempt with invalid parameter set');
		return $a;
	}

	// get db connection
	$conn = getConnection();
	if (!$conn) {
		return $a;
	}

	// get requesting user
	$result = getUserByBoth($conn, $both);
	if (!$result) {
		return $a;
	}

	// get user data
	$row = pg_fetch_array($result, 0, PGSQL_ASSOC);
	$userid = $row['id'];
	$uname = $row['username'];
	$auth = $row['auth'];
	$access = $row['access'];
	$email = $row['email'];

	// get TIC
	$publicTic = generateTic();
	$hashTic = hashTic($publicTic);

	// send TIC to user by email
	$boo = sendAuthenticationEmail($email, $publicTic, 'reset');
	if (!$boo) {
		$a['status'] = 'send-email-failed';
		return $a;
	}

	// set new auth
	$auth = DB::$auth_resetpending;

	// update user record
	$name = 'change-user-auth';
	$sql = "update account.user set auth = $1, hashtic=$3 where id = $2";
	$params = array($auth, $userid, $hashTic);
	$result = execSql($conn, $name, $sql, $params, true);
	if (!$result) {
		return $a;
	}

	// write a new session id token
	$si = writeToken($conn, $userid);
	if (!$si) {
		return $a;
	}

	// success
	$a['status'] = 'ok';
	$a['si'] = $si;
	$a['auth'] = $auth;
	$a['access'] = $access;
	$a['uname'] = $uname;
	return $a;
}
?>
