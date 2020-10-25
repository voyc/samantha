<?php
function changepassword() {
	$a = array(
	    'status' => 'system-error'
	);

	// raw inputs
	$taint_si = isset($_POST['si']) ? $_POST['si'] : 0;
	$taint_pword = isset($_POST['pword']) ? $_POST['pword'] : 0;
	$taint_pnew = isset($_POST['pnew']) ? $_POST['pnew'] : 0;

	// validate inputs
	$si = validateToken($taint_si);
	$pword = validatePword($taint_pword);
	$pnew = validatePword($taint_pnew);

	if (!$si || !$pword || !$pnew) {
		Log::write(LOG_WARNING, "attempt with invalid parameter set");
		return $a;
	}

	$conn = getConnection();
	if (!$conn) {
		return $a;
	}

	// get logged-in user
	$result = getUserByToken($conn, $si);
	if (!$result) {
		return $a;
	}

	// get data fields
	$row = pg_fetch_array($result, 0, PGSQL_ASSOC);
	$id = $row['id'];
	$dbpw = $row['hashpassword'];
	$auth = $row['auth'];

	// verify good user
	if (!isUserVerified($auth)) {
		Log::write(LOG_NOTICE, "attempt by non-verified user");
		return $a;
	}

	// verify password
	$boo = verifyPassword($pword, $dbpw);
	if (!$boo) {
		Log::write(LOG_NOTICE, "attempt with bad password");
		return $a;
	}

	// hash the new password
	$hashPassword = hashPassword($pnew);

	// update the user record
	$name = 'change-user-password';
	$sql  = "update account.user set hashpassword = $1 where id = $2";
	$params = array($hashPassword, $id);
	$result = execSql($conn, $name, $sql, $params, true);
	if (!$result) {
		return $a;
	}

	// success
	$a['status'] = 'ok';
	return $a;
}
?>
