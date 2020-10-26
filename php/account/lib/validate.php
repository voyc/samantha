<?php
/*
	validation functions.
*/

// public token is alphameric characters, plus, equals, slash.  Length 64 to 255.  (base64 encoded)
function validateToken($taint) {
	$clean = false;
	$ok = preg_match('/^[a-zA-Z0-9\+\=\/]{64,255}$/', $taint);
	if ($ok) {
		$clean = $taint;
	}
	return $clean;
}

// public temporary identification code is subset of characters. Length 6.
function validateTic($taint) {
	$clean = false;
	$ok = preg_match('/^[ACEFHJKMNPRTUVWXY4937]{6}$/', $taint);
	if ($ok) {
		$clean = $taint;
	}
	return $clean;
}

// bool is either t or f
function validateBool($taint) {
	$clean = false;
	if ($taint == 't' || $taint == 'f') {
		$clean = $taint;
	}
	return $clean;
}

// username is alphameric chars or underscore.  Length 6-64.
function validateUname($taint) {
	$clean = false;
 	$ok = preg_match('/^[a-zA-Z0-9\_]{6,64}$/', $taint);
	if ($ok) {
		$clean = $taint;
	}
	return $clean;
}

// use php email filter.  Length 6-100.
function validateEmail($taint) {
	$clean = false;
	$boo = filter_var($taint, FILTER_VALIDATE_EMAIL);
	if ($boo && strlen($taint) > 6 && strlen($taint) < 101) {
		$clean = $taint;
	}
	return $clean;
}

// might be email or username. alphameric chars, underscore, at, dot.  Length 6-64.
function validateBoth($taint) {
	$clean = false;
 	$ok = preg_match('/^[a-zA-Z0-9\_@.]{6,64}$/', $taint);
	if ($ok) {
		$clean = $taint;
	}
	return $clean;
}

// pword is alphameric chars plus some punctuation.  Length 4-255.
function validatePword($taint) {
	$clean = false;
 	$ok = preg_match('/^[a-zA-Z0-9@&#$%]{4,255}$/', $taint);
	if ($ok) {
		$clean = $taint;
	}
	return $clean;
}

function isUserAnonymous($auth) {
	return ($auth == DB::$auth_anonymous);
}
function isUserRegistered($auth) {
	return ($auth == DB::$auth_registered);
}
function isUserResetPending($auth) {
	return ($auth == DB::$auth_resetpending);
}
function isUserEmailPending($auth) {
	return ($auth == DB::$auth_emailpending);
}
function isUserVerified($auth) {
	return ($auth == DB::$auth_verified);
}
function wasUserVerified($auth) {
	return ($auth >= DB::$auth_verified);
}
?>
