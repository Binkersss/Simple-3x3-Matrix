import math

matrix = [['a1','b1','c1'],['a2','b2','c2'],['a3','b4','c3']]

for item in matrix:
	print(item) 

a1 = input('Enter a1:')
b1 = input('Enter b1:')
c1 = input('Enter c1:')
a2 = input('Enter a2:')
b2 = input('Enter b2:')
c2 = input('Enter c2:')
a3 = input('Enter a3:')
b3 = input('Enter b3:')
c3 = input('Enter c3:')

new = [[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]]

for item in new:
	print(item) 

def matrix_multiply(a1, b1, c1, a2, b2, c2, a3, b3, c3):
	a1 = int(a1)
	b1 = int(b1)
	c1 = int(c1)
	a2 = int(a2)
	b2 = int(b2)
	c2 = int(c2)
	a3 = int(a3)
	b3 = int(b3)
	c3 = int(c3)
	product = (a1*b2*c3 + b1*c2*a3 + c1*a2*b3) - (a3*b2*c1 + b3*c2*a1 + c3*a2*b1)
	print("Matrix Solution: " + str(product))

matrix_multiply(a1, b1, c1, a2, b2, c2, a3, b3, c3)
	
