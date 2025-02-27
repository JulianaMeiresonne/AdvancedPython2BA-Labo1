import math 
from scipy import integrate as itg
def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n < 0: 
		raise ArithmeticError()
	fact_value = math.factorial(n)
	return fact_value

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta = (b**2)- (4*a*c) # !!! ** = mettre au carré donc b^2 = b**2
	print(delta)
	if delta == 0 :
		return ((-b + math.sqrt(delta))/(2*a))
	elif delta > 0:
		return ((-b - math.sqrt(delta))/(2*a),(-b + math.sqrt(delta))/(2*a))
	elif delta <0:
		return (0)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	
	def fun(x):
		return eval(function)
	result = itg.quad(fun, lower, upper)
	return result[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1/3, -2, 3))
	print(integrate('x ** 2 - 1', -1, 1))

#!!! une fois qu'on commit un fichier sur git, il continue à le tracker meme si on le met apres sur gitignore