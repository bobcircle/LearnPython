# 這是一個計算BMI的程式，用來練習if elif els

heigh = input('請輸入身高(cm):')
heigh = float(heigh)/100	
weight = input('請輸入體重(kg):')
weight = float(weight)
bmi = weight / (heigh * heigh)  #bmi計算公式:體重(kg)/身高(m)平方
print('你的BMI為:', bmi)
if bmi < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('正常')
elif bmi >= 24 and bmi < 27:
	print('體重過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')