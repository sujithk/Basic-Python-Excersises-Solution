def pal(n):
	s=0
	c=n
	while(n>0):
		b=n%10
		s=s*10+b
		n=n/10
	if (s==c):
		return ("number is palindrome")
	else:
		return ("number is not palindrome")



print pal(909)	
