"""
Problem1: Prefix averages
"""


# Ouadratic time complexity n + [(n-1) + (n-2) + .... + 3 + 2 + 1]
# Time complexity: O(n^2)
def prefix_average1(S):
    n = len(S)
    a = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += S[j]
        a[i] = total / (i + 1)
    return a


# print(prefix_average1([1,2,3,4]))
# Still quadratic time complexity
def prefix_average2(S):
    n = len(S)
    a = [0] * n
    for i in range(n):
        a[i] = sum(S[0:i+1]) / (i + 1)
    return a


# Linear time complexity
def prefix_average3(S):
    n = len(S)
    a = [0] * n
    total = 0
    for i in range(n):
        total += S[i]
        a[i] = total / (i+1)
    return a


"""
Problem2: Disjoint Sets
"""


# Time complexity of O(n^3)
def disjoint1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


# Time complexity of O(n^2)
def disjoint2(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


"""
Problem3: Element uniqueness
"""


# Time complexity O(n^2)
def unique1(S):
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if S[i] == S[j]:
                return False
    return True


# Time compelxity of O(nlogn): Provided the array is SORTED
# Same elements will be located together
def unique2(S):
    temp = sorted(S)  # time complexity of O(nlogn)
    for i in range(1, len(temp)):
        if temp[i-1] == temp[i]:
            return False
    return True

print(unique2([1, 2, 3, 4, 5]))