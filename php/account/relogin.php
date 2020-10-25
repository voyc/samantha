<?php
/**
	svc relogin
	Login a previously logged-in user.
*/
function relogin() {
	$a = array(
	    'status' => 'system-error'
	);

	// get raw inputs
	$taint_si = isset($_POST['si']) ? $_POST['si'] : 0;

	// validate inputs
	$si = validateToken($taint_si);

	// validate parameter set
	if (!$si) {
		Log::write(LOG_WARNING, 'attempt with invalid parameter set');
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
	$uname = $row['username'];
	$auth = $row['auth'];
	$access = $row['access'];

	// verify auth
	if (!isUserVerified($auth)) {
		Log::write(LOG_NOTICE, "non-verified user has logged in");
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
