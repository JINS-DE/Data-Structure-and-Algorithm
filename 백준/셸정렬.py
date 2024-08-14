
a=[8,5,4,2,7,6,3,1]
n=len(a)
h=n//2

while h>0:
	for i in range(h,n):
		j = i-h
		tmp = a[i]
		while j >=0 and a[j] > tmp:
			a[j+h] = a[j]
			j-=h
		a[j+h]=tmp
		print(a)
	h//=2
	
print(n//9)