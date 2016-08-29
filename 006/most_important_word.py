# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os
import re

def words_counter(filepath):
	word = re.compile(r'([a-zA-Z]+)')
	dict = {}
	with open(filepath, 'r') as file:
		content = file.read()
		for words in word.findall(content):
			if words not in dict:
				dict[words] = 1
			else:
				dict[words] += 1
	list_sorted = sorted(dict.items(), key=lambda x:x[1], reverse=True)
	return list_sorted

def diary_statistic(filepath):
	diary_path = []
	for diary_name in os.listdir(filepath):
		diary_path.append(os.path.join(filepath,diary_name))
	with open('/python/daily/006/statistic.txt', 'w') as file:
		for diary in diary_path:
			ls = words_counter(diary)
			file.write('three most important words and the appearance times in '+diary+'/n')
			for i in range(3):
				dt = '/t'+ls[i][0]+': '+str(ls[i][1])+'/n'
				file.write(dt)

if __name__ == '__main__':
	filename = '/python/daily/006/diary'
	diary_statistic(filename)
	