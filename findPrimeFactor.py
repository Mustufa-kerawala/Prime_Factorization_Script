import math

def get_prime_factors(n):
	factors = list()
	for i in range(2,n):
		if n % i == 0:
			factors.append(i)
	print(factors)

def gcd_Euclid(a, b):
	#Base case
	if(a == 0):
		return b, 0, 1

	gcd, x1, y1 = gcd_Euclid(b%a, a) #Unpacking variables during recursion
	
	#Updating x and y using the results of recursive call
	x = y1 - (b//a) * x1
	y = x1

	return gcd, x, y



#Driver code
a, b = 90, 100
factor, x, y = gcd_Euclid(90, 100)

print("{} a, {} b, {} factor".format(x, y, factor))

get_prime_factors(83)
