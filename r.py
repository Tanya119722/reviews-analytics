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
print(d,len(d))
print('the avg length of the reviews is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'reviews less than 100 letters')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are', len(good), 'reviews mentioned good')
print(good[0])