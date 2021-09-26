"""
Year is a leap year
"""

def is_leap(year):
	leap = False

	if (year%4) == 0:
		if (year%100) == 0:
			if (year%400) == 0:
				leap = True
		else:
			leap = True

	return leap

"""
String concatenation
for 3 return
123
"""

def f(n):
	l = ''
	for i in range(1, n+1):
		l = l+str(i)
	return l


if __name__ == "__main__":
	print(is_leap(1992))