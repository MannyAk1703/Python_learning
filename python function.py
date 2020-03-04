def myfunc (a,b):
	if  a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)
print(myfunc (4,7))

#First letters the same True or False
def animal_crackers (a,b):
	return a[0] == b[0]
print (animal_crackers('gack','gohn'))

#Does it make 20 True or False 
def makes_twenty (a,b):
	return a+b == 20 or a == 20 or b == 20
print (makes_twenty(8,86))

#First and third letter capital 
def capital (a):
	return a[:3].capitalize() + a[3:].capitalize()
print(capital('abcdef'))

#Master yoda function 
def master_yoda (a):
	return ' '.join(a.split()[::-1])
print(master_yoda('i am home'))

def near (n):
 return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print(near(89))

def balckjack (a,b,c):
	if a+b+c <= 21:
		return a+b+c
	elif a+b+c<=31 and 11 in (a,b,c):
		return a+b+c -10 
	elif a+b+c >= 21:
		return 'BUST'

print(balckjack(11,10,10))

def paper_doll (a):
	result  = ''
	for char in a:
		result += char *3 
	return result
print(paper_doll(''))
