# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

import string

class senseword():
	def __init__(self):
		self.list = []
		with open('/python/daily/0011/filtered_words.txt', 'r') as file:
			for line in file.readlines():
				self.list.append(line)
		self.list = map(string.strip, self.list)
		for item in self.list:
			print item
			
	def checkword(self, word):
		for item in self.list:
			if item == word:
				return True
		return False

if __name__ == '__main__':
	mycheck = senseword()
	while True:
		str = raw_input('Please enter a word: ')
		if str:
			if (mycheck.checkword(str)):
				print 'Freedom'
			else:
				print 'humanRight'
		else:
			break