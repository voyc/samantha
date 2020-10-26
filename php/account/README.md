# account
User Authentication

A library of AJAX services for user management:

  * register
  * verify
  * login
  * relogin
  * logout
  * forgotpassword
  * resetpassword
  * changeusername
  * changepassword
  * changeemail
  * verifyemail

A git submodule.<br/>
Written in PHP and Postgres.<br/>
Includes a demo/test UI for developers.<br/>
See the Model project for an example of how this submodule is included in a complete UI framework.

## Design Principles

  1. This project is open source.  The source code for this library is provided publicly on github so it can be vetted by multiple experts, and so the security algorithms do not depend on obfuscation and are not susceptible to reverse-engineering.
  
  1. Sensitive information including seeds and database credentials is placed in the config file, and the config file is not included in the git repository and is not on the docroot path.

  1. The directory structure is organized so the server-side PHP code is not exposed on the docroot path.

  1. A second-stage email verification is required after register, changeemail, and resetpassword requests.

  1. It is recommended that anonymous users be allowed to use the application, but database saves are executed only for verified users.

  1. For PHP server configuration security, we rely on our hosting service.

  1. We do NOT use PHP sessions.  Instead we create our own session-id "token".

  1. We DO use PHP password_hash() and password_verify() with the default parameters.  Algorithm and random-generated salt are concatenated to the hash in the returned value.

  1. All database access is done with prepared statements.

  1. All POST inputs to services are filtered on the server immediately.

  1. Error codes from the services contain minimal information.

  1. All http requests use POST method.

  1. It is recommended that all http requests are made to an SSL server with a valid certificate, though this is recommended but not enforced by this application.
  
  1. CORS is implemented so that service requests from a non-SSL server can be serviced by this app running on an SSL server.

  1. Tokens do not contain unhashed database keys.

  1. It is recommended the token be stored in local storage instead of cookie, so it is not carried in an http header of every server request.

  1. Valid inputs are enforced
    . valid email address: includes @ and .
    . valid password: between 4 and 64 chars
	. valid username: between 4 and 64 chars
  
  1. User's password and email are never returned to the client.
  
## Summary of Threats and Mitigation

**Threat:** SQL injection.<br/>
**Mitigation:** All user inputs are filtered on the server before use.  All SQL is executed with prepared statements.

**Threat:** Password cracking, using databases of stolen password hashes.<br/>
**Mitigation:** A seed is concatenated with user's password.

**Threat:** Password guessing.<br/>
**Mitigation:** Detect, limit, and log failed attempts.

**Threat:** Password probing attack can become a DOS attack unintentionally.<br/>
**Mitigation:** ?

**Threat:** Leaking server setup details.<br/>
**Mitigation:** Limited error codes returned to client.  Details of errors written to server log, not to client.

**Threat:** Timing attacks.  Example: login attempt with existing username takes longer to respond.<br/>
**Mitigation:** We query for username/password combination with a single query.

**Threat:** Session Hijacking
**Mitigation:** 
  1. Session-id is replaced on any svc call after n minutes.
  1. Session-Id times out after n minutes of inactivity.
  1. Session-Id times out after n minutes since login.

## Unsupported Features:
The following features are NOT supported.

  1. Remember me.  Save username, and fill in the login form next time.
  1. Stay signed in.  Save the session-id or equivalent between sessions.
  1. Unrecognized computer.  Require email verification if user logs in with previously unused ip/user-agent.
  1. Multiple simultaneous sessions.  User logs in on different computers or browsers.
  1. Auto logout.  Use HTTP Push to log the user out and erase the screen on timeout.
		
## Categories
Security,
Privacy,
User Authentication,
Code Hiding,
ID Theft,
PHP,
AJAX

