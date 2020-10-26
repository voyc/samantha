<?php
/**
	replacement for syslog

	Log::write() wraps native php error_log()
		input $code is ignored.

	error_log type
		0, to apache errorlog, or echoed to console
		1, to designated email
		2, not used
		3, to designated file
		4, to SAPI handler

	syslog() severity levels
		0	LOG_EMERG	system is unusable (not for use by applications)
		1	LOG_ALERT	action must be taken immediately
		2	LOG_CRIT	critical conditions
		3	LOG_ERR		error conditions
		4	LOG_WARNING	warning conditions
		5	LOG_NOTICE	normal, but significant, condition
		6	LOG_INFO	informational message
		7	LOG_DEBUG	debug-level message

	our usage
		LOG_CRIT	db down
		LOG_ERR		possible database corruption
		LOG_WARNING	likely intrusion 
		LOG_NOTICE	likely intrusion only if occurring in large numbers
		LOG_INFO	open, close
		email is sent to admin on warning, err, and crit, not on notice or info
**/

class Log {
	public static $svcname = '';
	
	public static function open($svcname) {
		self::$svcname = $svcname;
		self::write(LOG_INFO, 'open');
	}

	public static function close($status) {
		self::write(LOG_INFO, "close $status");
		self::$svcname = '';
	}

	public static function write($severity, $msg) {
		// format the message
		$m = date(DATE_RFC2822) . ', ' . self::$svcname . ", $severity, $msg\n";

		// write the message to log
		error_log($m, 3, Config::$log_logfile);

		// write severe errors to email
		if ($severity <= LOG_WARNING) {
			error_log($m, 1, Config::$log_email);  // to email
		}
	}
}
?>
