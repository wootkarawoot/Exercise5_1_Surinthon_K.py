ItemIphone11 = 'IPHONE 11'
ItemPriceIphone11 = 40000

ItemIpadPro = 'IPAD PRO'
ItemPriceIpadPro = 37000

ItemTvLg5D = 'TV LG 5D'
ItemPriceTvLg5D = 25000


InputUser = input('กรุณกรอกชื่อผู้ใช้')
InputPasswordUser = input('กรุณากรอกรหัสผ่าน')

if InputUser == 'karawoot' and InputPasswordUser =='1':
	print('login success')
	print('Hello',InputUser)
	
	print('----shop-W-------')
	print('สินค้าทั้งหมด')
	print('1.',ItemIphone11,'ราคา:',ItemPriceIphone11,'บาท')
	print('2.',ItemIpadPro, 'ราคา:',ItemPriceIpadPro,'บาท')
	print('3.',ItemTvLg5D,'ราคา:',ItemPriceTvLg5D,'บาท')
	InputchoiceShop = int(input('กรุณาเลือกรายการสั่งซื้อสินค้า(กรุณาระบุตัวเลข (1-3):'))
	
	if InputchoiceShop <=3 and InputchoiceShop!= 0:
		
		if InputchoiceShop == 1:
			InputCountIphone = int(input('คุณเลือก IPHONE11 ต้องการจำนวนกี่ชิ้น'))
			
			print('สรุปรายการสั่งซื้อ')
			print(ItemIphone11 ,'ราคา',ItemPriceIphone11,'บาท,จำนวน',InputCountIphone,'ชิ้น ราคาทั้งหมด' ,ItemPriceIphone11*InputCountIphone,'บาท')
			
		elif InputchoiceShop == 2:
			InputCountIpad = int(input('คุณเลือก IPADPRO ต้องการกี่ชิ้น'))
			
			print('สรุปรายการสั่งซื้อ')
			print('IpadPro ราคา',ItemPriceIpadPro,'บาท,จำนวน',InputCountIpad,'ชิ้น ราคาทั้งหมด' ,ItemPriceIpadPro*InputCountIpad)
			
		elif InputchoiceShop == 3:
			InputCountTv = int(input('คุณเลือก TVLG 5D ต้องการกี่ชิ้น'))
			print('สรุปรายการสั่งซื้อ')
			print(ItemTvLg5D,'ราคา',ItemPriceTvLg5D,'บาทจำนวน',InputCountTv,'ชิ้น ราคาทั้งหมด',ItemPriceTvLg5D*InputCountTv)
	else:
		print('สินค้ามีแค่ลำดับ1-3 คุณเลือกไม่ถูกต้อง กรุณาเข้าสู่ระบบใหม่แล้วลองอีกครั้ง')

	
			
else:
	print('user or password not correct')
