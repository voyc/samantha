/* 
This SQL is designed for postgres.

After creating this schema, execute the GRANT statements found in the comments section of the config.php file.
*/

/* drop schema account cascade; */
create schema account;

create table account.user (
	id serial primary key,
	username varchar(100) not null,
	email varchar(100) not null,
	hashpassword varchar(255) not null,
	auth integer not null default 0,
	access integer not null default 1,
	tmregister timestamp with time zone not null default now(),
	tmverify timestamp with time zone,
	hashtic varchar(100),
	tmhashtic timestamp with time zone,
	newemail varchar(100)
);
create unique index ndx_username on account.user (username);
create unique index ndx_email on account.user (email);

create table account.token (
	id serial primary key,
	userid integer not null default 0,
	token varchar(64),
	tmcreate timestamp with time zone not null default now(),
	tmreplace timestamp with time zone,
	tmactive timestamp with time zone,
	tmexpire timestamp with time zone,
	ipcreate varchar(39) not null default '0.0.0.0',
	agentcreate varchar(255)
);
create unique index ndx_token on account.token (token);

create table account.attempt (
	id serial primary key,
	reason char(2) not null default '',
	userid integer not null default 0,
	tm timestamp with time zone not null default now(),
	ip varchar(39) not null default '0.0.0.0',
	agent varchar(255)
);
