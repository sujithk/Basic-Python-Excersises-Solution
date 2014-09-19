def fact(x):
	n=[x]+range(1,x)
	p=1
	for v in n:
		p=p*v
	return p


print fact(4)

