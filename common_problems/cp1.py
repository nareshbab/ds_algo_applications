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


if __name__ == "__main__":
	# print(is_leap(1992))
	# print(is_prime(482))
	# print(list_primes(30))
	print(custom_sqrt(99, 5))