def sum_from_1_to_100():
	s = 0
	for i in range(1, 101):
		s += i
	return s

def sum_from_1_squared_to_1000_squared():
	s = 0
	for i in range(1, 1001):
		s += i**2
	return s

def Factorielle(n):
	s = 1
	for i in range(2, n+1):
		s *= i
	return s

def func_d(a):
	s = 1
	n = 1
	while (s < a):
		n += 1
		s += n * (n + 1)
	return n

def min_div(x):
	d = 2
	while (x % d != 0):
		d += 1
	return d

def base_count(x, b):
	n = 1
	while x // b != 0:
		n += 1
		x //= b
	return n

def prime_list(n):
	p = 2
	while (n != 1):
		if n % p == 0:
			print(p)
			while n % p == 0:
				n //= p
		p += 1
	return 0

print(sum_from_1_to_100())
print(sum_from_1_squared_to_1000_squared())
print(Factorielle(4))
print(min_div(49))
print(base_count(1234, 64))
print("prime list")
prime_list(1234)
