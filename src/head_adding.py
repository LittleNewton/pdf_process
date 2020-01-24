f = open('FreePic2Pdf_bkmk.txt', 'r')

# 将所有的行读入一个列表
tmp = f.readline()
l = []
while (tmp):
	l.append(tmp)
	tmp = f.readline()
# 字符数组
n = [	'0',
	'1',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'习']
new = []
# 记录数据
count = 0
prefix = ''
for i in l:
	if (i[0] == '\t' and i[1] in n):
		new.append(i)
		prefix = (((i.split(' '))[0]).split('\t'))[1]
		count = 0
	elif (i[0] == '\t' and i[1] == '\t' and i[2] not in n):
		count = count + 1
		P = prefix + '.' + str(count) + ' '
		new.append('\t\t' + P + i[2:])
	else:
		new.append(i)
		pass

f = open('o.txt', 'w')
for i in new:
	f.write(i)