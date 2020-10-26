<?php
/**
	svc changeemail
	Request a different email.
*/
function changeemail() {
	$a = array(
	    'status' => 'system-error'
	);

	// get raw inputs
	$taint_si = isset($_POST['si']) ? $_POST['si'] : 0;
	$taint_pword = isset($_POST['pword']) ? $_POST['pword'] : 0;
	$taint_email = isset($_POST['email']) ? $_POST['email'] : 0;

	// validate inputs
	$si = validateToken($taint_si);
	$pword = validatePword($taint_pword);
	$email = validateEmail($taint_email);

	// validate parameter set
	if (!$si || !$pword || !$email) {
		Log::write(LOG_WARNING, "attempt with invalid parameter set");
		return $a;
	}

	// get db connection
	$conn = getConnection();
	if (!$conn) {
		return $a;
	}

	// get logged-in user
	$result = getUserByToken($conn, $si);
	if (!$result) {
		return $a;
	}

	// get user data
	$row = pg_fetch_array($result, 0, PGSQL_ASSOC);
	$userid = $row['id'];
	$hashpassword = $row['hashpassword'];
	$auth = $row['auth'];
	$oldemail = $row['email'];

	// verify auth
	if (!isUserVerified($auth) && !isUserEmailPending($auth)) {
		Log::write(LOG_NOTICE, "attempt by non-verified user");
		return $a;
	}

	// verify password
	$boo = verifyPassword($pword, $hashpassword);
	if (!$boo) {
		Log::write(LOG_NOTICE, "attempt with invalid password");
		return $a;
	}

	// verify email is unique
	$name = 'test-unique-email';
	$sql  = "select id from account.user where email = $1 and id <> $2";
	$params = array($email, $userid);
	$result = execSql($conn, $name, $sql, $params, false);
	if (!$result) {
		return $a;
	}
	$numrows = pg_num_rows($result);
	if ($numrows > 0) {
		Log::write(LOG_NOTICE, "$name: email already on file");
		$a['status'] = 'email-in-use';
		return $a;
	}

	// get TIC
	$publicTic = generateTic();
	$hashTic = hashTic($publicTic);

	// send TIC to user by email
	$boo = sendAuthenticationEmail($email, $publicTic, 'verifyemail');
	if (!$boo) {
		$a['status'] = 'send-email-failed';
		return $a;
	}

	// set new auth
	$auth = DB::$auth_emailpending;

	// update user record
	$name = 'change-user-email';
	$sql  = "update account.user set newemail = $1, auth=$3, hashtic=$4, tmhashtic=now() where id = $2";
	$params = array($email, $userid, $auth, $hashTic);
	$result = execSql($conn, $name, $sql, $params, true);
	if (!$result) {
		return $a;
	}

	// success
	$a['status'] = 'ok';
	$a['auth'] = $auth;
	return $a;
}
?>
