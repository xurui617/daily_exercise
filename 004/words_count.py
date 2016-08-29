# count all the english words in a txt file

import re

def words_count(filepath):
	with open(filepath, 'r') as f:  # use with to open and close file
		file = f.read()
		words = re.compile(r'([a-zA-Z]+)')  # use re to refine the rule of words
		d = {}        # use a dictionary; keys---words, values---times appeared
		for i in words.findall(file):
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		d_sorted = sorted(d.items(), key=lambda x:x[1], reverse=True)  # use sorted to sort the dictionary by values in descending order and finally return a list
		return d_sorted

if __name__ == '__main__':
	filepath = '/python/daily/004/POI.txt'
	for items in words_count(filepath):
		print "%s: %d" % (items[0], items[1])