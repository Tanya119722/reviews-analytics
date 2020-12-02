data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('all reviews have been read, there are', len(data), 'in total')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print(sum_len)

print('the avg length of the reviews is', sum_len/len(data))