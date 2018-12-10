class MaxSizeList(object):

	def __init__(self, max_length):
		self.max_length = max_length
		self.lst = []

	def push(self, text):
		self.lst.append(text)
		if len(self.lst) > self.max_length:
			self.lst.pop(0)
			
	def get_list(self):
		return self.lst