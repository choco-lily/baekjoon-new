a, b = map(int, input().split())
r = '=='
if a > b:
	r = '>'
if a < b:
	r = '<'
print(r)