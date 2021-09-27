import math


def is_leap(year):
	"""
	Year is a leap year
	"""
	leap = False

	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				leap = True
		else:
			leap = True

	return leap


def f(n):
	"""
	String concatenation
	for 3 return
	123
	"""
	nstr = ''
	for i in range(1, n + 1):
		nstr = nstr + str(i)
	return nstr


def is_prime(n):
	"""
	Is Prime or not
	ex: 12
	2*6
	3*4
	4*3
	6*2
	since 2*4 is equal to 4*2 so we dont need to check twice.
	Hence we need to check till sqrt(n)
	"""
	prime = True
	if n == 1:
		prime = False
	c = 2
	while c * c <= n:
		if n % c == 0:
			prime = False
		c += 1
	return prime


def list_primes(n):
	"""
	Print all the prime numbers till n
	"""
	arr = [True] * n
	arr[0] = False
	arr[1] = False
	for i in range(2, int(math.sqrt(n)) + 1):
		if is_prime(i):
			for j in range(2 * i, n, i):
				arr[j] = False
	primes = []
	for i in range(len(arr)):
		if arr[i]:
			primes.append(i)
	return primes


def custom_sqrt(n, p):
	"""
	Find sqrt of a number
	n -> number
	p -> precision for the sqrt
	"""
	start = 0
	end = n
	while start <= end:
		mid = start + (end - start) // 2
		if mid*mid == n:
			return mid
		if mid * mid > n:
			end = mid - 1
		if mid * mid < n:
			start = mid + 1

	root = end
	incr = 0.1
	for i in range(p):
		while (root*root <= n):
			root += incr

		root -= incr
		incr /= 10

	return root


def newton_sqrt(n, threshold):
	"""
	Find sqrt of a number
	n -> number
	threshold -> error threshold which we can tolerate
	"""
	x = n
	while True:
		root = 0.5 * (x + n/x)

		if abs(root - x) < threshold:
			return root

		x = root


def factors1(n):
	factors = []
	for i in range(1, n+1):
		if n%i == 0:
			factors.append(i)
	return factors


def factors2(n):
	"""Loop till sqrt of the number"""
	factors = []
	i = 1
	while i <= math.sqrt(n):
		if n%i == 0:
			factors.append(i)
			factors.append(n/i)
		i += 1
	return factors


def gcd(a, b):
	"""
	Returns greatest common factor/divisor for a & b
	"""
	if a == 0:
		return b

	return gcd(b%a, a)


def lcm(a, b):
	"""
	Returns the least common multiplier of a & b
	formula: lcm * (hcf or gcd) = a * b
	"""

	return (a * b)/gcd(a, b)



if __name__ == "__main__":

	# print(is_leap(1992))
	# print(is_prime(482))
	# print(list_primes(30))
	# print(custom_sqrt(99, 5))
	# print(newton_sqrt(99, 0.3))
	# print(factors1(20))
	# print(factors2(20))
	print(gcd(9, 21))