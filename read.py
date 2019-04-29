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
for d in data :
	sum_len = sum_len + len(d)
print('留言平均長度為',sum_len / len(line),'個字')
