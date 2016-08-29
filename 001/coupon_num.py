import random, string

f = open('coupon_num.txt', 'a')   # under windows, open in this way to make final writing change lines
for i in range(200):
	chars = string.letters + string.digits   # generate a string "a~zA~Z0~9"
	list = [random.choice(chars) for i in range(10)]  # generate a ten digits number
	coupon_num = ''.join(list)
	f.write(coupon_num)
	f.write('\n')
f.close()