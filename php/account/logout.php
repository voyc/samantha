<?php
/**
	svc logout
	Logout user.
*/
function logout() {
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

	// invalidate user session-id
	$boo = expireToken($conn, $si);
	if (!$boo) {
		return $a;
	}

	// success
	$a['status'] = 'ok';
	return $a;
}
?>
