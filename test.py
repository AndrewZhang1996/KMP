from KMP import kmp 

patterns = 'Alexander'

filename = 'book.txt'
contents = ''

with open(filename) as f_obj:
	contents=f_obj.read()

kmp_search = kmp(contents, patterns)

kmp_search.get_next()

results = kmp_search.get_results()

if results != -1:
	print('Found '+str(len(results))+' Results')
	print('Results: ')
	for result in results:
		line = ''
		for i in range(result-10, result+len(patterns)+10):
			line+=contents[i]
		print(line)
		print('-------------------------------------------------')
else:
	print('No results!')
