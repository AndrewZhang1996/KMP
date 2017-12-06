class kmp():

	def __init__(self, string, pattern):
		self.string = string
		self.pattern = pattern
		self.results = []
		self.string_mark = 0

	def get_next(self):   # 8m-7
		next = range(len(self.pattern)) # 1
		next[0] = -1 # 1
		i = 0 # 1
		k = -1 # 1
		while i < len(self.pattern)-1: # 2m-3
			if k == -1 or self.pattern[i] == self.pattern[k]: # 2m-3
				i += 1 # m-1 
				k += 1 # m-1
				next[i] = k # m-1
			else:
				k = next[k] # m-2
		return next

	def kmp(self): # 2m+6n-5
		if len(self.pattern) == 0: # 1
			return 0

		#get next
		next = self.get_next() # 8m-7

		#start search
		j = 0 # 1
		while self.string_mark < len(self.string) and j < len(self.pattern): # 2(n-m)
			if j == -1 or self.string[self.string_mark] == self.pattern[j]: # n-m
				self.string_mark += 1 # n-m
				j += 1 # n-m
			else:
				j = next[j] # n-m

		#if matching succeed
		if j == len(self.pattern):
			self.results.append(self.string_mark - len(self.pattern))
			self.kmp()
		else:	
			return -1

	def get_results(self):
		self.kmp()
		return self.results

