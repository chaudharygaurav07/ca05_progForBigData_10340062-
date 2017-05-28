#CA5
import math

def sum(values): # sum of a list of values
	return reduce(lambda x, y: x + y, values)
	
def max(values):
	return reduce(lambda a,b: a if (a > b) else b, values)

def min(values):
	return reduce(lambda a,b: a if (a < b) else b, values)

def add(first, second):
	return map(lambda x, y: x + y, first, second) 
	
def is_even(values):
	return filter(lambda x: x%2 == 0, values)
	
def divide(first, second):
	return map(lambda x, y: x/float(y) if y != 0 else 'nan', first, second)
	

def greater_than_mean_2(values):
	mean = sum(values)/len(values) #calculating the mean before passing it in
	return filter(lambda x: x > mean, values)

def circum(rad):
	return map(lambda x: x * 2 * math.pi, rad)
	

def to_farenheit(values):
	return [ ((float(9)/5) * x + 32) for x in values ]

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit

#fibonacci series based on desired length
def fibonacci(n):

	a,b = 0,1
	counter = 0
	while True:
		if (counter > n): return
		yield a
		a, b = b, a + b
		counter += 1
		
input = raw_input("upto what numbers do you want fibonacci series \n")
input = int(input)
f = fibonacci(input)
for number in f: #this will automatically call f.next
	print number



	
"Passing values and testing"
	
print sum([10, 11, 12, 13])
print max([10, 11, 12, 13])
print min([10, 11, 12, 13])
print add([10, 11, 12, 13], [10, 15, 8, 25])
print is_even([10, 11, 12, 13])
print divide([4, 5, 6], [2, 1, 0])
print greater_than_mean_2([10, 11, 12, 13])
print circum([10, 11, 12, 13])



