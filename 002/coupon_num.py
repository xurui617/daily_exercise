import random, string
import sqlite3

conn = sqlite3.connect('coupon_number.db')
cursor = conn.cursor()
cursor.execute('create table coupon_number (id integer primary key, number varchar(10))')
lis = []

f = open('coupon_num.txt', 'a')   # under windows, open in this way to make final writing change lines

for i in range(200):
	chars = string.letters + string.digits   # generate a string "a~zA~Z0~9"
	list = [random.choice(chars) for j in range(10)]  # generate a ten digits number; use j instead of i in second loop
	coupon_num = ''.join(list)
	f.write(coupon_num)
	f.write('\n')
	
	tpl = (i+1, coupon_num)
	lis.append(tpl)

cursor.executemany('insert into coupon_number (id, number) values (?, ?)', lis)
conn.commit()
cursor.close()
conn.close()
f.close()