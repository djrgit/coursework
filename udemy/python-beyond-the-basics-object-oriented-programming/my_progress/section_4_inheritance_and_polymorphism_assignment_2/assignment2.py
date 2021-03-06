import abc
from datetime import datetime

class WriteFile(object):
	
	__metaclass__ = abc.ABCMeta

	def __init__(self, filename, delim=None):
		self.filename = filename
		self.delim = delim

	@abc.abstractmethod
	def write(self, data):
		return


class LogFile(WriteFile):

	def dt_str(self):
		self.dt = datetime.now().strftime('%Y-%m-%d %H:%M')
		return self.dt

	def write(self, data):
		with open(self.filename, 'a+') as f:
			f.write('{}    {}\n'.format(self.dt_str(), data))


class DelimFile(WriteFile):

	def write(self, data):
		with open(self.filename, 'a+') as f:
			f.write(self.delim.join(data) + '\n')
