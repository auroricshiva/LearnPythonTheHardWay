i = 0
numbers = []

while i < 6:
	print("At the top i is %d" % i)
	numbers.append(i)
	
	i += 1
	print("Numbers now: ", numbers)
	print("At the bottom i is %d" % i)
	print()

print("The numbers: ")

for num in numbers:
	print(num)

def do_while_less_than(n, incr = 1):
	i = 0
	numbers = []
	
	while i < n:
		print("At the top i is %d" % i)
		numbers.append(i)
		
		i += incr
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)
		print()

do_while_less_than(1000, 10)

def print_until(n):
	for i in range(0, n):
		print("The number is at: %d" % i)

print_until(40)