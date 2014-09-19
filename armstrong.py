def armstng(n):
	s=0
	c=n
	while(n>0):
		b=n%10
		s=s+b*b*b
		n=n/10
	if (c==s):
		return ("no is armsng")
	else:
		return ("no is not armsng")

print armstng(153)



