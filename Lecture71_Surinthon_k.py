menuList = []
PriceList = []

def showBill():
	print("----------เมนู อาหาร----------")
	for number in range(len(menuList)):
		print(number,'ทดสอบ')
		print(menuList[number],PriceList[number],' บาท')
	TotalPrice = 0
	for x in PriceList:
		TotalPrice = TotalPrice + int(x)
	print('ราคาทั้งหมด :',TotalPrice, ' บาท')
		
	
while True:
	menuName = input("โปรดเลือกเมนู :")
	if menuName.lower() == "exit":
		break
	else:
		menuPrice = input("โปรดใส่ราคา")
		menuList.append(menuName)
		PriceList.append(menuPrice)
		
		
showBill()
