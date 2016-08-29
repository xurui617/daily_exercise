# 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import string, random

# 字体的路径
fontpath = '/Windows/Fonts/Arial/arialbd.ttf'


# 产生随机的四个字母
def getRandomchar():
	return [random.choice(string.letters) for i in range(4)]

# 产生随机的颜色
def getRandomcolor():
	return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))

# 获得验证图片
def getCodePicture():
	# 定义画布
	width = 240
	height = 60
	image = Image.new('RGB', (width, height), (180, 180, 180))
	font = ImageFont.truetype(fontpath, 40)
	draw = ImageDraw.Draw(image)
	# 产生随机四个字母，并用随机的颜色，花在特定的位置
	code = getRandomchar()
	for i in range(4):
		draw.text((60 * i + 10, 0), code[i], font=font, fill=getRandomcolor())
	# 填充一定数量的噪点
	for j in range(random.randint(1500, 3000)):
		draw.point((random.randint(0, width), random.randint(0, height)), fill = getRandomcolor())
	# 把图像模糊处理并保存
	image = image.filter(ImageFilter.BLUR)
	image.save(''.join(code) + '.jpg', 'jpeg')

if __name__ == '__main__':
	getCodePicture()