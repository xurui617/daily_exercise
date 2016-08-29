# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os

def change_size(filepath):
	for pict in os.listdir(filepath):
		pictpath = os.path.join(filepath, pict)
		with Image.open(pictpath) as im:
			w, h = im.size
			index = w/1136 if w/1136 > h/640 else h/640
			im.thumbnail((w/index, h/index))
			im.save('finished_' + pict.split('.')[0] + '.jpg', 'jpeg')

if __name__ == '__main__':
	filepath = '/python/daily/005/pics'
	change_size(filepath)