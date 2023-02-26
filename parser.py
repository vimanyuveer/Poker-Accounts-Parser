text_file = open('/Users/vimanyu/Desktop/poker_records.txt')
text = text_file.read()

def pairwise_It(iterator):
	# convert to an iterator so we can iterate over the list
	iterator = iter(iterator)
	# loops over the entire list to produce pairs of values
	while True:
		# send two values at a time
		try:
			yield next(iterator), next(iterator)
		except StopIteration:
		# stop when no more iterators are there
			return

def acc_Parse(text):
	names = ['aman', 'vimanyu', 'shaurya', 'nihar', 'puru', 'shrey', 'somin']
	accounts = {name:0 for name in names}
	# NOT SPLITTING THE TEXT PROPERLY!
	for a, b in pairwise_It(text.split(" ", '/n')):
		print(a, b)
		# adds to the accounts dict if the pattern matches
		if (a.lower() in names) and ('+' in b or '-' in b):
			accounts[a] += float(b)
			print("FLAG")
	print(accounts)

acc_Parse(text)
