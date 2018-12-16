import os

class ConfigDict(dict):

	def __init__(self, filename):

		self._filename = filename
		if os.path.exists(self._filename):
			with open(self._filename, 'r') as f:
				for line in f:
					line = line.rstrip()
					key, val = line.split('=', 1)
					dict.__setitem__(self, key, val)

	def __setitem__(self, key, val):
		
		dict.__setitem__(self, key, val)
		with open(self._filename, 'w') as f:
			for key, val in self.items():
				f.write('{0}={1}\n'.format(key, val))