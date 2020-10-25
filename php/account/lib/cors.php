<?php
function writeHeader() {
	if (Config::$allowLocalTesting) {
		header("Access-Control-Allow-Origin: *");
		return;
	}

	$origin = (isset($_SERVER['HTTP_ORIGIN'])) ? $_SERVER['HTTP_ORIGIN'] : '';
	if (in_array($origin, Config::$allowedOrigins)) {
		header("Access-Control-Allow-Origin: $origin");
	}
}
?>