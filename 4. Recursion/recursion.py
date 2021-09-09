"""
Problem: Factorial
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


"""
Problem: English ruler
"""


def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length"""
    line = "_" * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """Draw an english ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, num_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))



"""
Problem: Binary Search
"""


def binary_search(data, target, low, high):
    """

    Args:
        data:
        target:
        low:
        high:

    Returns:
        True if the target is found in the data list

    """

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target > data[mid]:
            return binary_search(data, target, mid+1, high)
        else:
            return binary_search(data, target, low, mid -1)


def binary_search_iterative(data, target):
    """Returns True if target is found in the python list"""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


"""
Problem: Directory size
"""
import os


def disk_usage(path):
    """Returns the cummulative size of a directory"""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    return total


"""
Problem: Inefficient Recursions
"""


# For every call there are 2 subsequent calls resulting in O(2^n) time complexity
def unique3(S, start, stop):
    """Returns True if there are no duplicates in the data list"""
    if stop - start <= 1: return True
    elif not unique3(S, start, stop - 1): return False
    elif not unique3(S, start + 1, stop): return False
    else: return S[start] != S[stop - 1]


def bad_fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n < 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


def good_fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)


"""
Problem: Linear sum
"""


def linear_sum(S, n):
    """Returns the sum of first n numbers"""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


"""
Problem: Reverse sequence
"""


# Time complexity of O(n)
def reverse(S, start, stop):
    """Reverses elements in implicit slice"""
    if start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)


def reverse_iterative(S):
    """Reverses elements in implicit slice"""
    start, stop = 0, len(S) - 1
    while start < stop:
        S[start], S[stop] = S[stop], S[start]
        start, stop = start + 1, stop - 1



"""
Problem: Power [Linear recursion]
"""


# Time complexity of O(n)
def power1(x, n):
    """Returns the nth power of x"""
    if n == 0:
        return 1
    return x * power1(x, n-1)


# Time complexity of O(logn)
def power2(x, n):
    """Returns the nth power of x"""
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


"""
Problem: Binary sum [Binary recursion]
"""


# Time complexity of O(logn)
def binary_sum(S, start, stop):
    """Returns the sum of the numbers in S[start:stop]"""
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)








