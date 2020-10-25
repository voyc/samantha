/* drop schema mai cascade; */
create schema mai;

create table mai.profile (
	id serial primary key,
	userid integer,
	displayname varchar(50),
	gender char(1),
	photo varchar(250),
	phone varchar(20)
);

create table mai.vocab (
	id serial primary key,
	userid integer,
	language char(2),
	type char(1),
	word varchar(100),
	state char(1),
	recency bigint,
	mastery integer
);

create table mai.dict (
	id serial primary key,
	g char(1),          /* type o:one-syllable, m:multi-syllable */
	t varchar(100),     /* thai */
        tl varchar(100),    /* translit */
	tlm char(1),        /* translit method a:auto, m:manual */
        cp varchar(100),    /* components, csv */
	cpm char(1),        /* components method, a:auto, m:manual */
        ru varchar(100),    /* rules, csv */
	lvl int default 100,/* level 1 to 100  */
	org char(1)         /* origin, s:sanskrit, etc. */
);
create table mai.mean (
	id serial primary key,
	did int,            /* foreign key to dict table */
	n int,              /* num of definition, 1-based index */
	s int,              /* source 0:unspecified, 1:, 2:, 3: */
	l int,              /* level, 0 to 1000 */
	p varchar(9),       /* pos, part of speech, nvjeipr */
	e varchar(100),     /* english word, gloss */
	d varchar(500)      /* details */
);

create sequence mai.dict_id_seq;
select setval('mai.dict_id_seq',  (select max(id) from mai.dict));
create sequence mai.mean_id_seq;
select setval('mai.mean_id_seq',  (select max(id) from mai.mean));

create table mai.alphabet (
	id serial primary key,
	t char(1),	/* thai glyph */
	e varchar(4),	/* english translit */
	u char(6),	/* unicode */
	r char(1),	/* reference, for sanskrit consonant, the equivalent consonant */
	m char(1),	/* m:class
				m:middle class consonant
				l:low class consonant
				h:high class consonant
				v:vowel
				u:unknown for glyph
				o:obsolete glyph: ฃ, ฅ
				s:symbol glyph: ฿, ๆ, ฯ 
				t:tonemark
				d:digit */
	a char(1)	/* subclass
				s:sonorant consonant
				a:diacritic above
				b:diacritic below
				l:diacritic left
				r:diacritic right */
);
create unique index alphabet_t_index on mai.alphabet(t);

create table mai.story (
	id serial primary key,
	authorid int,		/* foreign key to user table */
	title varchar(100),
	language char(2),	/* constant "th" */
	original text,
	meta text,              /* comments about the story */
	words text,
	titleeng varchar(100),
	avglvl int,
	maxlvl int,
	components text,
	numwords int,
	numwordsnew int,
	numcomponents int,
	numcomponentsnew int
);
create unique index story_title_index on mai.story(title);

