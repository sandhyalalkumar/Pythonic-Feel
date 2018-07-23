for _ in range(input()):
	n=input()
	a=map(int,raw_input().split())
	a.sort()
	c=1
	for i in range(1,n):
		if a[i]>a[i-1]:
			c+=1
	print c