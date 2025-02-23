a, b = input().split(' ')
a = int(a); b = int(b)
r = '=='
if a > b:
	r = '>'
if a < b:
	r = '<'
print(r)