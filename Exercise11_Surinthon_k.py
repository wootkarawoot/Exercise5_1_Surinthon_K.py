UserInput = int(input('inputNumberPeramit:' ))
Star = '*'
Blank = ' '

for Round in range(UserInput):
	BlankLeft= (Blank*(UserInput-(Round+1)))
	StarCount = Star*(Round+1)
	StarRight = Star*Round
	 
	Peramit = BlankLeft+StarCount+StarRight
	print(Peramit)




	'''

	(จริงๆผมจะใช้แบบนี้ครับ แต่ทำเสร็จอ่านยากหน่อย555เลยทำแบบด้านบนคับ)
        for Round in range(UserInput):
	
	Peramit= (Blank*(UserInput-(Round+1)))+(Star*(Round+1))+(Star*Round)
	
	print(Peramit)
	

	'''
