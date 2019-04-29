data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1   # count = count + 1
		if count % 100000 == 0:
			print(len(data))
			print(line)

sum_len = 0
for d in data :    #d:每筆留言  data:裝著留言的清單
	sum_len = sum_len + len(d)
print('留言平均長度為',sum_len / len(data),'個字')

new = []
new_1 = []
for d in data:
	if len(d) < 100:   
		new.append(d)   #把長度<100的留言裝進清單"new = [ ]"裡面
	

print(len(new))
print('共有',len(new),'筆資料長度小於100')

