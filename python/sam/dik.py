''' dik.py - s3 starter dictionary '''
pos = {
	'noun': 'noun', 
	'pron': 'pronoun',
	'name': 'proper noun',
	'verb': 'verb', 
	'adj':  'adjective', 
	'adv':  'adverb', 
	'prep': 'preposition', 
	'intj': 'interjection', 
	'conj': 'conjunction',
	'qw'  : 'conjunction',
}

'''
Python NTLK

CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent’s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO, to go ‘to’ the store.
UH interjection, errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when


https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
Alphabetical list of part-of-speech tags used in the Penn Treebank Project:
Note:  these are the 'modified' tags used for Penn tree banking; these are the tags used in the Jet system. NP, NPS, PP, and PP$ from the original Penn part-of-speech tagging were changed to NNP, NNPS, PRP, and PRP$ to avoid clashes with standard syntactic categories.

	1.	CC	Coordinating conjunction
	2.	CD	Cardinal number
	3.	DT	Determiner
	4.	EX	Existential there
	5.	FW	Foreign word
	6.	IN	Preposition or subordinating conjunction
	7.	JJ	Adjective
	8.	JJR	Adjective, comparative
	9.	JJS	Adjective, superlative
	10.	LS	List item marker
	11.	MD	Modal
	12.	NN	Noun, singular or mass
	13.	NNS	Noun, plural
	14.	NNP	Proper noun, singular
	15.	NNPS	Proper noun, plural
	16.	PDT	Predeterminer
	17.	POS	Possessive ending
	18.	PRP	Personal pronoun
	19.	PRP$	Possessive pronoun
	20.	RB	Adverb
	21.	RBR	Adverb, comparative
	22.	RBS	Adverb, superlative
	23.	RP	Particle
	24.	SYM	Symbol
	25.	TO	to
	26.	UH	Interjection
	27.	VB	Verb, base form
	28.	VBD	Verb, past tense
	29.	VBG	Verb, gerund or present participle
	30.	VBN	Verb, past participle
	31.	VBP	Verb, non-3rd person singular present
	32.	VBZ	Verb, 3rd person singular present
	33.	WDT	Wh-determiner
	34.	WP	Wh-pronoun
	35.	WP$	Possessive wh-pronoun
	36.	WRB	Wh-adverb


http://phrasesinenglish.org/POScodes.html
British National Corpus

1	AJ0	adjective (general or positive) e.g. good, old
2	AJC	comparative adjective e.g. better, older
3	AJS	superlative adjective, e.g. best, oldest
4	AV0	adverb (general, not sub-classified as AVP or AVQ), e.g. often, well, longer, furthest.
5	AVP	adverb particle, e.g. up, off, out.
6	AVQ	wh-adverb, e.g. when, how, why, whether the word is used interrogatively or to introduce a relative clause.
7	CJC	coordinating conjunction, e.g. and, or, but.
8	CJS	subordinating conjunction, e.g. although, when.
9	CJT	the subordinating conjunction that, when introducing a relative clause, as in the day that follows Christmas.
10	CRD	cardinal numeral, e.g. one, 3, fifty-five, 6609.
11	ORD	ordinal numeral, e.g. first, sixth, 77th, next, last.
12	AT0	article, e.g. the, a, an, no.
13	DPS	possessive determiner form, e.g. your, their, his.
14	DT0	general determiner: a determiner which is not a DTQ e.g. this both in This is my house and This house is mine.
15	DTQ	wh-determiner, e.g. which, what, whose, which, whether used interrogatively or to introduce a relative clause.
16	NN0	common noun, neutral for number, e.g. aircraft, data, committee.
17	NN1	singular common noun, e.g. pencil, goose, time, revelation.
18	NN2	plural common noun, e.g. pencils, geese, times, revelations.
19	NP0	proper noun, e.g. London, Michael, Mars, IBM.
20	PNI	indefinite pronoun, e.g. none, everything, one (pronoun), nobody.
21	PNP	personal pronoun, e.g. I, you, them, ours. possessive pronouns such as ours and theirs are included in this category.
22	PNQ	wh-pronoun, e.g. who, whoever, whom.
23	PNX	reflexive pronoun, e.g. myself, yourself, itself, ourselves.
24	POS	the possessive or genitive marker 's or ', tagged as a distinct word.
25	PRF	the preposition of.
26	PRP	preposition, other than of, e.g. about, at, in, on behalf of, with. Prepositional phrases like on behalf of or in spite of treated as single words.
27	VBB	the present tense forms of the verb be, except for is or 's: am, are 'm, 're, be (subjunctive or imperative), ai (as in ain't).
28	VBD	the past tense forms of the verb be: was, were.
29	VBG	-ing form of the verb be: being.
30	VBI	the infinitive form of the verb be: be.
31	VBN	the past participle form of the verb be: been
32	VBZ	the -s form of the verb be: is, 's.
33	VDB	the finite base form of the verb do: do.
34	VDD	the past tense form of the verb do: did.
35	VDG	the -ing form of the verb do: doing.
36	VDI	the infinitive form of the verb do: do.
37	VDN	the past participle form of the verb do: done.
38	VDZ	the -s form of the verb do: does.
39	VHB	the finite base form of the verb have: have, 've.
40	VHD	the past tense form of the verb have: had, 'd.
41	VHG	the -ing form of the verb have: having.
42	VHI	the infinitive form of the verb have: have.
43	VHN	the past participle form of the verb have: had.
44	VHZ	the -s form of the verb have: has, 's.
45	VM0	modal auxiliary verb, e.g. can, could, will, 'll, 'd, wo (as in won't)
46	VVB	the finite base form of lexical verbs, e.g. forget, send, live, return. This tag is used for imperatives and the present subjunctive forms, but not for the infinitive (VVI).
47	VVD	the past tense form of lexical verbs, e.g. forgot, sent, lived, returned.
48	VVG	the -ing form of lexical verbs, e.g. forgetting, sending, living, returning.
49	VVI	the infinitive form of lexical verbs , e.g. forget, send, live, return.
50	VVN	the past participle form of lexical verbs, e.g. forgotten, sent, lived, returned.
51	VVZ	the -s form of lexical verbs, e.g. forgets, sends, lives, returns.
52	EX0	existential there, the word there appearing in the constructions there is..., there are ....
53	ITJ	interjection or other isolate, e.g. oh, yes, mhm, wow.
54	TO0	the infinitive marker to.
55	UNC	unclassified items which are not appropriately classified as items of the English lexicon.
56	XX0	the negative particle not or n't.
57	ZZ0	alphabetical symbols, e.g. A, a, B, b, c, d.
58	-*-	"wildword" matching any PoS tag (non-standard extension for phrase-frame queries and result sets).
'''

sdik = [
	# s3              pos       parent            en               th
	('root'         ,'noun'   , None            ,'root'          ,'ราก'               ),
	('empty'        ,'adj'    ,'root'           ,'empty'         ,'ว่าง'               ),
	('person'       ,'noun'   ,'root'           ,'person'        ,'คน'                ),
	('place'        ,'noun'   ,'root'           ,'place'         ,'สถานที่'             ),
	('thing'        ,'noun'   ,'root'           ,'thing'         ,'สิ่ง'                ),
	('action'       ,'noun'   ,'root'           ,'action'        ,'หนังบู๊'              ),
	('link'         ,'noun'   ,'root'           ,'link'          ,'ลิงค์'               ),

	('typeof'       ,'prep'   ,'link'           ,'typeof'        ,'ประเภทของ'         ),
	('of'           ,'prep'   ,'link'           ,'ownedby'       ,'ของ'               ),
	('by'           ,'prep'   ,'link'           ,'by'            ,'โดย'               ),
	('to'           ,'prep'   ,'link'           ,'to'            ,'ที'                 ),

	('question'     ,'noun'   ,'link'           ,'question'      ,'คำถาม'             ),
	('which'        ,'adv'    ,'question'       ,'which'         ,'ที่'                 ),   # apply to noun
	('where'        ,'adv'    ,'question'       ,'where'         ,'ที่ไหน'              ),   # apply to verb
	('why'          ,'adv'    ,'question'       ,'why'           ,'ทำไม'              ),
	('when'         ,'adv'    ,'question'       ,'when'          ,'เมื่อไหร่'            ),   # default "now"
	('how'          ,'adv'    ,'question'       ,'how'           ,'อย่างไร'            ),
	('what'         ,'adv'    ,'question'       ,'what'          ,'อะไร'              ),   # applies only to "do"

	('this'         ,'adj'    ,'which'          ,'this'          ,'นี้'                 ),
	('next'         ,'adj'    ,'which'          ,'next'          ,'ต่อไป'              ),
	('last'         ,'adj'    ,'which'          ,'last'          ,'ล่าสุด'              ),   # previous

	('time_period'  ,'noun'   ,'thing'          ,'time_period'   ,'ช่วงเวลา'           ),
	('week'         ,'noun'   ,'time_period'    ,'week'          ,'สัปดาห์'             ),
	('day'          ,'noun'   ,'time_period'    ,'day'           ,'วัน'                ),
	('month'        ,'noun'   ,'time_period'    ,'month'         ,'เดือน'              ),
	('year'         ,'noun'   ,'time_period'    ,'year'          ,'ปี'                 ),

	('time'         ,'noun'   ,'thing'          ,'time'          ,'เวลา'              ),
	('now'          ,'adv'    ,'time'           ,'now'           ,'ตอนนี้'              ),
	('yesterday'    ,'adv'    ,'time'           ,'yesterday'     ,'เมื่อวานนี้'           ),
	('today'        ,'adv'    ,'time'           ,'today'         ,'วันนี้'               ),
	('tomorrow'     ,'adv'    ,'time'           ,'tomorrow'      ,'พรุ่งนี้'              ),
	('morning'      ,'adv'    ,'time'           ,'morning'       ,'ตอนเช้า'            ),
	('afternoon'    ,'adv'    ,'time'           ,'afternoon'     ,'ตอนบ่าย'            ),
	('evening'      ,'adv'    ,'time'           ,'evening'       ,'ตอนเย็น'            ),

	('you'          ,'pron'   ,'person'         ,'you'           ,'คุณ'                ),
	('I'            ,'pron'   ,'person'         ,'I'             ,'ผม'                ),
	('friend'       ,'pron'   ,'person'         ,'friend'        ,'เพื่อน'              ),
	('family'       ,'pron'   ,'person'         ,'family'        ,'ครอบครัว'           ),
	('name'         ,'noun'   ,'thing'          ,'name'          ,'ชี่อ'                ),
	('Nid'          ,'name'   ,'person'         ,'Nid'           ,'นิด'                ),
	('Pin'          ,'name'   ,'person'         ,'Pin'           ,'พิน'                ),
	('May'          ,'name'   ,'person'         ,'May'           ,'เมย์'               ),
	('Som'          ,'name'   ,'person'         ,'Som'           ,'ส้ม'                ),
	('Nui'          ,'name'   ,'person'         ,'Nui'           ,'นุ้ย'                ),
	('Memi'         ,'name'   ,'person'         ,'Memi'          ,'มีมี่'                ),
	('Fern'         ,'name'   ,'person'         ,'Fern'          ,'เฟร์น'              ),
	('Bella'        ,'name'   ,'person'         ,'Bella'         ,'เบลล่า'             ),
	('Jenny'        ,'name'   ,'person'         ,'Jenny'         ,'เจนนี่'              ),
	('Penny'        ,'name'   ,'person'         ,'Penny'         ,'เพนนี'              ),
	('Milky'        ,'name'   ,'person'         ,'Milky'         ,'มิ้ลกี้'               ),
	('Donut'        ,'name'   ,'person'         ,'Donut'         ,'โดนัท'              ),
	('Namtip'       ,'name'   ,'person'         ,'Namtip'        ,'น้ำทิพย์'             ),
	('Tangmo'       ,'name'   ,'person'         ,'Tangmo'        ,'แตงโม'             ),
	('Chompoo'      ,'name'   ,'person'         ,'Chompoo'       ,'ชมพู่'               ),
	('Naiyana'      ,'name'   ,'person'         ,'Naiyana'       ,'นัยนา'              ),
	('Sam'          ,'name'   ,'person'         ,'Sam'           ,'แซม'               ),
	('Joe'          ,'name'   ,'person'         ,'Joe'           ,'โจ'                ),
	('John'         ,'name'   ,'person'         ,'John'          ,'จน'                ),
	('Juan'         ,'name'   ,'person'         ,'Juan'          ,'ฆ'                 ),

	('city'         ,'noun'   ,'place'          ,'city'          ,'เมือง'              ),
	('island'       ,'noun'   ,'place'          ,'island'        ,'เกาะ'              ),
	('house'        ,'noun'   ,'place'          ,'house'         ,'บ้าน'               ),

	('businesstype' ,'noun'   ,'thing'          ,'businesstype'  ,'ประเภทธุรกิจ'        ),
	('bank'         ,'noun'   ,'businesstype'   ,'bank'          ,'ธนาคาร'            ),
	('coffeeshop'   ,'noun'   ,'businesstype'   ,'coffeeshop'    ,'ร้านกาแฟ'           ),
	('restaurant'   ,'noun'   ,'businesstype'   ,'restaurant'    ,'ร้านอาหาร'          ),
	('salon'        ,'noun'   ,'businesstype'   ,'salon'         ,'ร้านเสริมสวย'        ),
	('market'       ,'noun'   ,'businesstype'   ,'market'        ,'ตลาด'              ),
	('mall'         ,'noun'   ,'businesstype'   ,'mall'          ,'ห้างสรรพสินค้า'       ),
	('pharmacy'     ,'noun'   ,'businesstype'   ,'pharmacy'      ,'ร้านขายยา'          ),
	('cinema'       ,'noun'   ,'businesstype'   ,'cinema'        ,'โรงภาพยนตร์'        ),
	('doctor'       ,'noun'   ,'businesstype'   ,'doctor'        ,'หมอ'               ),
	('hospital'     ,'noun'   ,'businesstype'   ,'hospital'      ,'โรงพยาบาล'         ),
	('clinic'       ,'noun'   ,'businesstype'   ,'clinic'        ,'คลินิก'              ),
	('dentist'      ,'noun'   ,'businesstype'   ,'dentist'       ,'ทันตแพทย์'           ),
	('embassy'      ,'noun'   ,'businesstype'   ,'embassy'       ,'สถานทูต'            ),

	('Bangkok'      ,'name'   ,'city'           ,'Bangkok'       ,'กรุงเทพมหานคร'      ),
	('Phuket'       ,'name'   ,'city'           ,'Phuket'        ,'ภูเก็ต'              ),
	('Koh_Samui'    ,'name'   ,'island'         ,'Koh_Samui'     ,'เกาะสมุย'           ),
	('Krabi'        ,'name'   ,'city'           ,'Krabi'         ,'กระบี่'              ),
	('Pattaya'      ,'name'   ,'city'           ,'Pattaya'       ,'พัทยา'              ),
	('Hua_Hin'      ,'name'   ,'city'           ,'Hua_Hin'       ,'หัวหิน'              ),
	('Chiang_Mai'   ,'name'   ,'city'           ,'Chiang_Mai'    ,'เชียงใหม่'           ),
	('Pai'          ,'name'   ,'city'           ,'Pai'           ,'ปาย'               ),
	('Udon_Thani'   ,'name'   ,'city'           ,'Udon_Thani'    ,'อุดรธานี'            ),
	('Sukothai'     ,'name'   ,'city'           ,'Sukothai'      ,'สุโขทัย'             ),
	('Ayutthaya'    ,'name'   ,'city'           ,'Ayutthaya'     ,'อยุธยา'             ),

	('food'         ,'noun'   ,'thing'          ,'food'          ,'อาหาร'             ),
	('vacation'     ,'noun'   ,'thing'          ,'vacation'      ,'วันหยุดพักผ่อน'        ),
	('business'     ,'noun'   ,'thing'          ,'business'      ,'ธุรกิจ'              ),
	('money'        ,'noun'   ,'thing'          ,'money'         ,'เงิน'               ),
	('coffee'       ,'noun'   ,'food'           ,'coffee'        ,'กาแฟ'              ),
	('breakfast'    ,'noun'   ,'food'           ,'breakfast'     ,'อาหารเช้า'          ),
	('hair'         ,'noun'   ,'thing'          ,'hair'          ,'ผม'                ),
	('pedicure'     ,'noun'   ,'thing'          ,'pedicure'      ,'เล็บเท้า'            ),
	('manicure'     ,'noun'   ,'thing'          ,'manicure'      ,'ทำเล็บ'             ),
	('medicine'     ,'noun'   ,'thing'          ,'medicine'      ,'ยา'                ),
	('movie'        ,'noun'   ,'thing'          ,'movie'         ,'ภาพยนตร์'           ),
	('checkup'      ,'noun'   ,'thing'          ,'checkup'       ,'ตรวจสอบ'           ),
	('headache'     ,'noun'   ,'thing'          ,'headache'      ,'ปวดหัว'             ),
	('covid'        ,'noun'   ,'thing'          ,'covid'         ,'โควิด'              ),
	('tooth'        ,'noun'   ,'thing'          ,'tooth'         ,'ฟัน'                ),
	('teeth'        ,'noun'   ,'thing'          ,'teeth'         ,'ฟัน'                ),
	('filling'      ,'noun'   ,'thing'          ,'filling'       ,'การกรอก'           ),
	('whitening'    ,'noun'   ,'thing'          ,'whitening'     ,'ไวท์เทนนิ่ง'          ),
	('toothache'    ,'noun'   ,'thing'          ,'toothache'     ,'ปวดฟัน'             ),
	('braces'       ,'noun'   ,'thing'          ,'braces'        ,'จัดฟัน'              ),
	('fun'          ,'noun'   ,'thing'          ,'fun'           ,'สนุก'               ),

	('transport'    ,'noun'   ,'thing'          ,'transport'     ,'ขนส่ง'              ),
	('train'        ,'noun'   ,'transport'      ,'train'         ,'รถไฟ'              ),
	('bus'          ,'noun'   ,'transport'      ,'bus'           ,'รถบัส'              ),
	('airplane'     ,'noun'   ,'transport'      ,'airplane'      ,'เครื่องบิน'           ),
	('ship'         ,'noun'   ,'transport'      ,'ship'          ,'เรือ'               ),

	('Grab'         ,'name'   ,'transport'      ,'Grab'          ,'คว้า'               ),
	('car'          ,'noun'   ,'transport'      ,'car'           ,'รถยนต์'             ),
	('taxi'         ,'noun'   ,'transport'      ,'taxi'          ,'แท็กซี่'              ),
	('citybus'      ,'noun'   ,'transport'      ,'citybus'       ,'ซิตี้บัส'              ),
	('songtaew'     ,'noun'   ,'transport'      ,'songtaew'      ,'สองแถว'            ),
	('tuktuk'       ,'noun'   ,'transport'      ,'tuktuk'        ,'ตุ๊กตุ๊ก'              ),

	('walk'         ,'verb'   ,'action'         ,'walk'          ,'เดิน'               ),
	('run'          ,'verb'   ,'action'         ,'run'           ,'วิ่ง'                ),

	('do'           ,'verb'   ,'action'         ,'do'            ,'ทำ'                ),
	('go'           ,'verb'   ,'action'         ,'go'            ,'ไป'                ),
	('come'         ,'verb'   ,'action'         ,'come'          ,'มา'                ),
	('eat'          ,'verb'   ,'action'         ,'eat'           ,'กิน'                ),
	('visit'        ,'verb'   ,'action'         ,'visit'         ,'เยี่ยมชม'            ),
	('pickup'       ,'verb'   ,'action'         ,'pickup'        ,'ไปรับ'              ),
	('deliver'      ,'verb'   ,'action'         ,'deliver'       ,'ส่งมอบ'             ),
	('get'          ,'verb'   ,'action'         ,'get'           ,'ได้รับ'              ),
	('drink'        ,'verb'   ,'action'         ,'drink'         ,'ดื่ม'                ),
	('meet'         ,'verb'   ,'action'         ,'meet'          ,'พบกัน'              ),
	('wash'         ,'verb'   ,'action'         ,'wash'          ,'ล้าง'               ),
	('cut'          ,'verb'   ,'action'         ,'cut'           ,'ตัด'                ),
	('buy'          ,'verb'   ,'action'         ,'buy'           ,'ซื้อ'                ),
	('shop'         ,'verb'   ,'action'         ,'shop'          ,'ร้านค้า'             ),
	('watch'        ,'verb'   ,'action'         ,'watch'         ,'ดู'                 ),
	('fix'          ,'verb'   ,'action'         ,'fix'           ,'แก้ไข'              ),
	('test'         ,'verb'   ,'action'         ,'test'          ,'ทดสอบ'             ),
	('see'          ,'verb'   ,'action'         ,'see'           ,'ดู'                 ),
	('clean'        ,'verb'   ,'action'         ,'clean'         ,'สะอาด'             ),
	('remove'       ,'verb'   ,'action'         ,'remove'        ,'ลบ'                ),

	('cook'         ,'verb'   ,'action'         ,'cook'          ,'ปรุงอาหาร'          ),
	('brew'         ,'verb'   ,'action'         ,'brew'          ,'ชง'                ),
	('read'         ,'verb'   ,'action'         ,'read'          ,'อ่าน'               ),
	('listen'       ,'verb'   ,'action'         ,'listen'        ,'ฟัง'                ),
	('play'         ,'verb'   ,'action'         ,'play'          ,'เล่น'               ),
	('is'           ,'verb'   ,'action'         ,'is'            ,'คือ'                ),
	('feel'         ,'verb'   ,'action'         ,'feel'          ,'รู้สึก'               ),

	('relax'        ,'verb'   ,'action'         ,'relax'         ,'ผ่อนคลาย'           ),
	('chat'         ,'verb'   ,'action'         ,'chat'          ,'แชท'               ),
	('talk'         ,'verb'   ,'action'         ,'talk'          ,'พูด'                ),
	('give'         ,'verb'   ,'action'         ,'give'          ,'ให้'                ),

	('with'         ,'prep'   ,'link'           ,'with'          ,'กับ'                ),

	('have'         ,'verb'   ,'action'         ,'have'          ,'มี'                 ),
	('study'        ,'verb'   ,'action'         ,'study'         ,'ศึกษา'              ),
	('work'         ,'verb'   ,'action'         ,'work'          ,'ทำงาน'             ),

	('animal'       ,'noun'   ,'root'           ,'animal'        ,'สัตว์'               ),
	('cow'          ,'noun'   ,'animal'         ,'cow'           ,'วัว'                ),

	('foodtype'     ,'noun'   ,'root'           ,'foodtype'      ,'ประเภทอาหาร'       ),
	('rice'         ,'noun'   ,'foodtype'       ,'rice'          ,'ข้าว'               ),
	('tea'          ,'noun'   ,'foodtype'       ,'tea'           ,'ชา'                ),

	('book'         ,'noun'   ,'thing'          ,'book'          ,'หนังสือ'             ),
	('music'        ,'noun'   ,'thing'          ,'music'         ,'เพลง'              ),
	('game'         ,'noun'   ,'thing'          ,'game'          ,'เกม'               ),
	('homework'     ,'noun'   ,'thing'          ,'homework'      ,'การบ้าน'            ),
	('assignment'   ,'noun'   ,'thing'          ,'assignment'    ,'การมอบหมาย'        ),
	('computer'     ,'noun'   ,'thing'          ,'computer'      ,'คอมพิวเตอร์'         ),
	('job'          ,'noun'   ,'thing'          ,'job'           ,'งาน'               ),
	('garden'       ,'noun'   ,'thing'          ,'garden'        ,'สวน'               ),
	('weed'         ,'noun'   ,'thing'          ,'weed'          ,'วัชพืช'              ),
	('harvest'      ,'noun'   ,'thing'          ,'harvest'       ,'เก็บเกี่ยว'           ),
	('plant'        ,'noun'   ,'thing'          ,'plant'         ,'ปลูก'               ),

	('due'          ,'adj'    ,'thing'          ,'due'           ,'ครบกำหนด'          ),
	('many'         ,'adv'    ,'thing'          ,'many'          ,'มากมาย'            ),
	('howmuch'      ,'adv'    ,'link'           ,'howmuch'       ,'เท่าไหร่'            ),
	('too'          ,'adv'    ,'howmuch'        ,'too'           ,'เกิน'               ),

	('feeling'      ,'noun'   ,'root'           ,'feeling'       ,'ความรู้สึก'           ),
	('hungry'       ,'noun'   ,'feeling'        ,'hungry'        ,'หิว'                ),

	('kitchen'      ,'noun'   ,'place'          ,'kitchen'       ,'ครัว'               ),
	('backyard'     ,'noun'   ,'place'          ,'backyard'      ,'สนามหลังบ้าน'        ),
	('upstairs'     ,'noun'   ,'place'          ,'upstairs'      ,'ชั้นบน'              ),
	('bedroom'      ,'noun'   ,'place'          ,'bedroom'       ,'ห้องนอน'            ),
	('livingroom'   ,'noun'   ,'place'          ,'livingroom'    ,'ห้องนั่งเล่น'          ),

	('online'       ,'adv'    ,'place'          ,'online'        ,'ออน'               ),

	('command'      ,'noun'   ,'root'           ,'command'       ,'คำสั่ง'              ),
	('connect'      ,'verb'   ,'command'        ,'connect'       ,'โยงใย'             ),
	('password'     ,'noun'   ,'thing'          ,'password'      ,'รหัสผ่าน'            ),
	('translate'    ,'verb'   ,'command'        ,'translate'     ,'แปล'               ),
	('echo'         ,'verb'   ,'command'        ,'echo'          ,'เลียน'              ),
	('show'         ,'verb'   ,'command'        ,'show'          ,'แสดง'              ),
	('search'       ,'verb'   ,'command'        ,'search'        ,'ค้นหา'              ),
	('drill'        ,'verb'   ,'command'        ,'drill'         ,'ฝึก'                ),
]
