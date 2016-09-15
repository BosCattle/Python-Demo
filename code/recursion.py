
def recursion(n):
    sum = 1
    while n>0:
	sum = sum*n
	n = n-1
    return sum


def recursion1(n):
   if n==1:
	return 1
   return n*recursion1(n-1)
