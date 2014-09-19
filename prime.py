def prime(n):
	i=2
	p=0
	while(i<=n/2):
		i=i+1
		if ((n%i)==0):
			p=1
			return ("notprime")
	if p==0:
		return ("prime")
print prime(2)
