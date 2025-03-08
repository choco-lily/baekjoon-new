a = [1, 1, 2, 2, 2, 8]
b = input().split()
for i in range(0, 6):
	a[i] = str(a[i] - int(b[i]))
print(' '.join(a))