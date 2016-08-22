from PIL import Image, ImageDraw, ImageFont

from numpy import random    # use random to generate the number

def add_num(filepath, num=random.randint(10)):
	img = Image.open(filepath)
	size = img.size
	fontsize = size[1]/4        # set the size of font used
	myfont = ImageFont.truetype('/Windows/Fonts/Arial/arial.ttf', fontsize)            # font path should be the file exits in your system
	ImageDraw.Draw(img).text((3*fontsize, 0), str(num), font = myfont,fill='red')      # text(position, str) the position of the str
	img.save('pic1_num.jpg')
	img.show()

if __name__ == '__main__':
	filepath = '/python/daily/000/pic1.png'
	add_num(filepath)