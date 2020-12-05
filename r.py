import time
import progressbar

#read file
data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)		
print('all reviews have been read, there are', len(data), 'in total')


#avg len reviews
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(d,len(d))
print('the avg length of the reviews is', sum_len/len(data))

# reviews less than 100 letters
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'reviews less than 100 letters')

# word 'good' has been mentioned
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are', len(good), 'reviews mentioned good')
print(good[0])

# word count
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('spent', end_time - start_time, 'seconds')
print(len(wc))

# search a word
while True:
	word = input('what word are you looking for:')
	if word == 'q':
		break
	elif word in wc:
		print(word, 'has appared', wc[word], 'times')
	else:
		print('this word does not exist in the reviews')
print('thanks for using the search function')