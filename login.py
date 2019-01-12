#登入密碼確認，用於練習while迴圈
key = 'a123456'		#正確密碼
x = 3;
while x > 0:
	x -= 1
	password = input('請輸入密碼:')
	if password == key:
		print('登入成功')
		break
	else:
		if x == 0:
			print('密碼錯誤! 登入失敗 請稍後再試')
		else:
			print('密碼錯誤!還有', x, '次機會')