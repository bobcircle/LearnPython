# 資料分析練習
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完成，共', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')

good = [d for d in data if 'good' in d] # 等同於24-27行
# output = [運算 for 變數 in 清單 篩選條件 ]