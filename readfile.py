# 練習讀取檔案

with open ('test.txt', 'r') as file: # with是當離開open block會自動close
	for line in file:
		print(line.strip()) # strip() 去除空格與換行