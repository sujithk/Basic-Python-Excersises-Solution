def sprm(n):
	s=0
	p=0
	i=2
	while(i<=n/2):
		i=i+1
		if ((n%i)==0):
			p=1
			return ("n is not prime")

	if(p==0):
		while(n>0):
			b=n%10
			s=s+b
			n=n/10
	return s

print sprm(311)
				


