<?php
/**
	svc resetpassword
	Reset password.
*/
function resetpassword() {
	$a = array(
		'status' => 'system-error'
	);

	// get raw inputs
	$taint_si = isset($_POST['si']) ? $_POST['si'] : 0;
	$taint_tic = isset($_POST['tic']) ? $_POST['tic'] : 0;
	$taint_pnew = isset($_POST['pnew']) ? $_POST['pnew'] : 0;

	// validate inputs
	$si = validateToken($taint_si);
	$tic = validateTic($taint_tic);
	$pnew = validatePword($taint_pnew);

	// validate parameter set
	if (!$si || !$pnew || !$tic) {
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
	$hashtic = $row['hashtic'];
	$auth = $row['auth'];

	// verify auth
	if (!isUserResetPending($auth)) {
		Log::write(LOG_NOTICE, 'attempt by non-reset-pending user');
		$a['status'] = 'reset-fail';
		return $a;
	}

	// verify tic
	$boo = verifyTic($tic, $hashtic);
	if (!$boo) {
		Log::write(LOG_NOTICE, 'attempt with invalid tic');
		$a['status'] = 'reset-fail';
		return $a;
	}

	// hash the new password
	$hashpnew = hashPassword($pnew);

	// set new auth
	$auth = DB::$auth_verified;

	// update user record
	$name = 'reset-password-update';
	$sql = "update account.user set auth = $1, hashpassword = $3 where id = $2";
	$params = array($auth, $userid, $hashpnew);
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
