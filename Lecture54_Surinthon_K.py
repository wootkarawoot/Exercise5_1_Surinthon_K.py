UserName = 'karawoot'
PassWord = '12345'

ItemIphone11 = 30000
ItemTvLg = 45000
ItemIpad = 49000


def Login():
	UserInputLogin = input('กรุณาพิมพ์UserName:')
	UserInputPassW = input('กรุณาพิมพ์passWord:')
	while  UserInputLogin != UserName or UserInputPassW != PassWord:
		print('รหัสผ่านหรือUserไม่ถูกต้องกรุณาลองใหม่')
		UserInputLogin = input('กรุณาพิมพ์UserName:')
		UserInputPassW = input('กรุณาพิมพ์passWord:')
	if UserInputLogin == UserName and UserInputPassW == PassWord:
		pass
			
def ShowMenu():
	print('ข้อต้อนรับคุณ : ',UserName)
	print('กรุณาเลือกรายการสั่งซื้อสินค้า')
	print('--------------KShop-------------')
	print('1.IPHONE11 ราคา',ItemIphone11,' บาท')
	print('2.IpadPro ราคา',ItemIpad, ' บาท')
	print('3.TVLG 5D ราคา',ItemTvLg, ' บาท')
	return  ChoiceMenu()


def ChoiceMenu():
	UserInputChoice = int(input('กรุณาเลือกรายการสินค้า(1-3):'))
	while UserInputChoice == 0 or UserInputChoice > 3:
		print('กรอกเลขสินค้าผิด กรุณากรอกให้ตรง')
		UserInputChoice = int(input('กรุณาเลือกรายการสินค้า(1-3):'))
	if UserInputChoice ==1:
		print('คุณเลือก Iphone11 ราคา : ',str(ItemIphone11),'บาท')
		ChoiceOneCount = int(input('ต้องการสั่งซื้อสินค้ากี่ชิ้น:'))
		return CalculatorTotal(ItemIphone11,ChoiceOneCount)
		
	
	elif  UserInputChoice ==2:
		print('คุณเลือก IpadPro ราคา : ',str(ItemIpad),'บาท')
		ChoiceTwoCount = int(input('ต้องการสั่งซื้อสินค้ากี่ชิ้น:'))
		return CalculatorTotal(ItemIpad,ChoiceTwoCount)
	
	elif  UserInputChoice ==3:
		print('คุณเลือก TVLG 5 D ราคา : ',str(ItemTvLg),'บาท')
		ChoiceThreeCount = int(input('ต้องการสั่งซื้อสินค้ากี่ชิ้น:'))
		return  CalculatorTotal(ItemTvLg,ChoiceThreeCount)
			

	
def CalculatorVat(ToTalPrice):
	vat = 0.07
	resuft = ToTalPrice +(ToTalPrice*vat)
	return 'ราคารวมภาษี(Total) :'+str(int(resuft))+' บาท'


def CalculatorTotal(x,y):
	return CalculatorVat(x*y)
		
print(Login())
print(ShowMenu())
