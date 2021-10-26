def find_brute(string, pattern):
	"""
	Return first index of pattern in the string
	Time Complexity:    O(nm)
	"""
	n, m = len(string), len(pattern)

	for i in range(n - m + 1):
		k = 0
		while k < m and string[i + k] == pattern[k]:
			k += 1
		if k == m:
			return i
	return -1


print(find_brute("fabcabc", "abc"))