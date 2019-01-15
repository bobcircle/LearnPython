# 二維清單與寫檔練習
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price]) # 二維
print(products)

for p in products:
	print(p[0], '價格是', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
# csv 可以用Excel開啟，用,區隔內容