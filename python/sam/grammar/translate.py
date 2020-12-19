''' translate.py '''

class TranslateException(Exception):
	pass

class Translate:
	def getThai(self,sen):
		thai = []
		for each in sen.split(' '):
			thai.append(self.getThaiWord(each))
		return ' '.join(thai)

	def getEng(self,sen):
		eng = []
		for each in sen.split(' '):
			eng.append(self.getEngWord(each))
		return ' '.join(eng)

	def getThaiWord(self,eng):
		thai = ''
		try:
			thai = self.eng[eng]
		except:
			raise TranslateException (f'Cannot find Thai translation for English word: {eng}')
		return thai

	def getEngWord(self,thai):
		eng = ''
		try:
			eng = self.thai[thai]
		except:
			raise TranslateException (f'Cannot find English translation for Thai word: {thai}')
		return eng

	def setup(self):
		for row in self.table:
			self.eng[row[0]] = row[1]
			self.thai[row[1]] = row[0]

	def __init__(self):
		self.thai = {}
		self.eng = {}
		self.table = []
		self.loadtable()
		self.setup()

	def loadtable(self):
		self.table.append(['person'        ,'คน'  ]),             
		self.table.append(['place'         ,'สถานที่']),
		self.table.append(['thing'         ,'สิ่ง']),
		self.table.append(['action'        ,'หนังบู๊']),
		self.table.append(['link'          ,'ลิงค์']),
		self.table.append(['typeof'        ,'ประเภทของ']),
		self.table.append(['ownedby'       ,'ที่เป็นเจ้าของโดย']),
		self.table.append(['by'            ,'โดย']),
		self.table.append(['question'      ,'คำถาม']),
		self.table.append(['which'         ,'ที่']),
		self.table.append(['where'         ,'ที่ไหน']),
		self.table.append(['why'           ,'ทำไม']),
		self.table.append(['when'          ,'เมื่อไหร่']),
		self.table.append(['how'           ,'อย่างไร']),
		self.table.append(['what'          ,'อะไร']),
		self.table.append(['this'          ,'นี้']),
		self.table.append(['next'          ,'ต่อไป']),
		self.table.append(['last'          ,'ล่าสุด']),
		self.table.append(['time_period'   ,'ช่วงเวลา']),
		self.table.append(['week'          ,'สัปดาห์']),
		self.table.append(['day'           ,'วัน']),
		self.table.append(['month'         ,'เดือน']),
		self.table.append(['year'          ,'ปี']),
		self.table.append(['time'          ,'เวลา']),
		self.table.append(['now'           ,'ตอนนี้']),
		self.table.append(['yesterday'     ,'เมื่อวานนี้']),
		self.table.append(['today'         ,'วันนี้']),
		self.table.append(['tomorrow'      ,'พรุ่งนี้']),
		self.table.append(['morning'       ,'ตอนเช้า']),
		self.table.append(['afternoon'     ,'ตอนบ่าย']),
		self.table.append(['evening'       ,'ตอนเย็น']),
		self.table.append(['you'           ,'คุณ']),
		self.table.append(['I'             ,'ผม']),
		self.table.append(['friend'        ,'เพื่อน']),
		self.table.append(['Sam'           ,'แซม']),
		self.table.append(['John'          ,'จอห์น']),
		self.table.append(['Naiyana'       ,'นัยนา']),
		self.table.append(['Juan'          ,'ฆ']),
		self.table.append(['Joe'           ,'โจ']),
		self.table.append(['Nui'           ,'นุ้ย']),
		self.table.append(['Nid'           ,'นิด']),
		self.table.append(['city'          ,'เมือง']),
		self.table.append(['island'        ,'เกาะ']),
		self.table.append(['businesstype'  ,'ประเภทธุรกิจ']),
		self.table.append(['bank'          ,'ธนาคาร']),
		self.table.append(['coffeeshop'    ,'ร้านกาแฟ']),
		self.table.append(['restaurant'    ,'ร้านอาหาร']),
		self.table.append(['salon'         ,'ร้านเสริมสวย']),
		self.table.append(['market'        ,'ตลาด']),
		self.table.append(['mall'          ,'ห้างสรรพสินค้า']),
		self.table.append(['pharmacy'      ,'ร้านขายยา']),
		self.table.append(['cinema'        ,'โรงภาพยนตร์']),
		self.table.append(['doctor'        ,'หมอ']),
		self.table.append(['hospital'      ,'โรงพยาบาล']),
		self.table.append(['clinic'        ,'คลินิก']),
		self.table.append(['dentist'       ,'ทันตแพทย์']),
		self.table.append(['embassy'       ,'สถานทูต']),
		self.table.append(['house'         ,'บ้าน']),
		self.table.append(['Bangkok'       ,'กรุงเทพมหานคร']),
		self.table.append(['Phuket'        ,'ภูเก็ต']),
		self.table.append(['Koh_Samui'     ,'เกาะสมุย']),
		self.table.append(['Krabi'         ,'กระบี่']),
		self.table.append(['Pattaya'       ,'พัทยา']),
		self.table.append(['Hua_Hin'       ,'หัวหิน']),
		self.table.append(['Chiang_Mai'    ,'เชียงใหม่']),
		self.table.append(['Pai'           ,'ปาย']),
		self.table.append(['Udon_Thani'    ,'อุดรธานี']),
		self.table.append(['Sukothai'      ,'สุโขทัย']),
		self.table.append(['Ayutthaya'     ,'อยุธยา']),
		self.table.append(['food'          ,'อาหาร']),
		self.table.append(['vacation'      ,'วันหยุดพักผ่อน']),
		self.table.append(['business'      ,'ธุรกิจ']),
		self.table.append(['money'         ,'เงิน']),
		self.table.append(['coffee'        ,'กาแฟ']),
		self.table.append(['breakfast'     ,'อาหารเช้า']),
		self.table.append(['hair'          ,'ผม']),
		self.table.append(['pedicure'      ,'เล็บเท้า']),
		self.table.append(['manicure'      ,'ทำเล็บ']),
		self.table.append(['medicine'      ,'ยา']),
		self.table.append(['movie'         ,'ภาพยนตร์']),
		self.table.append(['checkup'       ,'ตรวจสอบ']),
		self.table.append(['headache'      ,'ปวดหัว']),
		self.table.append(['covid'         ,'โควิด']),
		self.table.append(['tooth'         ,'ฟัน']),
		self.table.append(['teeth'         ,'ฟัน']),
		self.table.append(['filling'       ,'การกรอก']),
		self.table.append(['whitening'     ,'ไวท์เทนนิ่ง']),
		self.table.append(['toothache'     ,'ปวดฟัน']),
		self.table.append(['braces'        ,'จัดฟัน']),
		self.table.append(['transport'     ,'ขนส่ง']),
		self.table.append(['train'         ,'รถไฟ']),
		self.table.append(['bus'           ,'รถบัส']),
		self.table.append(['airplane'      ,'เครื่องบิน']),
		self.table.append(['ship'          ,'เรือ']),
		self.table.append(['car'           ,'รถยนต์']),
		self.table.append(['Grab'          ,'คว้า']),
		self.table.append(['taxi'          ,'แท็กซี่']),
		self.table.append(['citybus'       ,'ซิตี้บัส']),
		self.table.append(['songtaew'      ,'สองแถว']),
		self.table.append(['tuktuk'        ,'ตุ๊กตุ๊ก']),
		self.table.append(['walk'          ,'เดิน']),
		self.table.append(['run'           ,'วิ่ง']),
		self.table.append(['go'            ,'ไป']),
		self.table.append(['come'          ,'มา']),
		self.table.append(['eat'           ,'กิน']),
		self.table.append(['visit'         ,'เยี่ยมชม']),
		self.table.append(['pickup'        ,'ไปรับ']),
		self.table.append(['deliver'       ,'ส่งมอบ']),
		self.table.append(['get'           ,'ได้รับ']),
		self.table.append(['drink'         ,'ดื่ม']),
		self.table.append(['meet'          ,'พบกัน']),
		self.table.append(['wash'          ,'ล้าง']),
		self.table.append(['cut'           ,'ตัด']),
		self.table.append(['buy'           ,'ซื้อ']),
		self.table.append(['shop'          ,'ร้านค้า']),
		self.table.append(['watch'         ,'ดู']),
		self.table.append(['fix'           ,'แก้ไข']),
		self.table.append(['test'          ,'ทดสอบ']),
		self.table.append(['see'           ,'ดู']),
		self.table.append(['clean'         ,'สะอาด']),
		self.table.append(['remove'        ,'ลบ']),
		self.table.append(['animal'        ,'สัตว์']),
		self.table.append(['cow'           ,'วัว']),
		self.table.append(['foodtype'      ,'ประเภทอาหาร']),
		self.table.append(['rice'          ,'ข้าว']),
		self.table.append(['tea'           ,'ชา']),
		self.table.append(['book'          ,'หนังสือ']),
		self.table.append(['music'         ,'เพลง']),
		self.table.append(['game'          ,'เกม']),
		self.table.append(['cook'          ,'ปรุงอาหาร']),
		self.table.append(['brew'          ,'ชง']),
		self.table.append(['read'          ,'อ่าน']),
		self.table.append(['listen'        ,'ฟัง']),
		self.table.append(['play'          ,'เล่น']),
		self.table.append(['is'            ,'คือ']),
		self.table.append(['feel'          ,'รู้สึก']),
		self.table.append(['feeling'       ,'ความรู้สึก']),
		self.table.append(['hungry'        ,'หิว']),
		self.table.append(['kitchen'       ,'ครัว']),
		self.table.append(['backyard'      ,'สนามหลังบ้าน']),
		self.table.append(['upstairs'      ,'ชั้นบน']),
		self.table.append(['bedroom'       ,'ห้องนอน']),
		self.table.append(['livingroom'    ,'ห้องนั่งเล่น']),
		self.table.append(['family'        ,'ครอบครัว'         ]),
		self.table.append(['Nid'           ,'นิด']),
		self.table.append(['Pin'           ,'พิน']),
		self.table.append(['May'           ,'เมย์']),
		self.table.append(['Som'           ,'ส้ม']),
		self.table.append(['Nui'           ,'นุ้ย']),       
		self.table.append(['Memi'          ,'มีมี่']),
		self.table.append(['Fern'          ,'เฟร์น']),
		self.table.append(['Bella'         ,'เบลล่า']),
		self.table.append(['Jenny'         ,'เจนนี่']),
		self.table.append(['Penny'         ,'เพนนี']),
		self.table.append(['Milky'         ,'มิ้ลกี้']),
		self.table.append(['Donut'         ,'โดนัท']),
		self.table.append(['Namtip'        ,'น้ำทิพย์']),
		self.table.append(['Tangmo'        ,'แตงโม']),
		self.table.append(['Chompoo'       ,'ชมพู่']),
		self.table.append(['Naiyana'       ,'นัยนา']),
		self.table.append(['Sam'           ,'แซม']),
		self.table.append(['Joe'           ,'โจ']),                                     
		self.table.append(['John'          ,'จอห์น']),                                     
		self.table.append(['Juan'          ,'ฆ']),                                     
		self.table.append(['chat'          ,'แชท']),
		self.table.append(['online'        ,'ออน']),
		self.table.append(['talk'          ,'พูด']),
		self.table.append(['with'          ,'กับ']),

'do', 'ทำ'
'homework',   'การบ้าน'
assignment due          ครบกำหนดวัน
assignment due          ครบกำหนดวัน
assignment due          ครบกำหนดวัน
study for test                    เรียนเพื่อทดสอบ
Why you work on computer?         ทำไมคุณถึงทำงานกับคอมพิวเตอร์?
for my job                        สำหรับงานของฉัน
Why you work in garden?           ทำไมคุณถึงทำงานในสวน?
too many weeds                    วัชพืชมากเกินไป
time for harvest                  ถึงเวลาเก็บเกี่ยว
time for planting                 เวลาปลูก                           


if __name__ == '__main__':
	tra = Translate()
	print(tra.getThaiWord('month'))
	print(tra.getEngWord('เดือน'))
	print(tra.getThai('Nid eat food where restaurant next month'))
	print(tra.getEng('นิด กิน อาหาร ที่ไหน ร้านอาหาร ต่อไป เดือน'))

