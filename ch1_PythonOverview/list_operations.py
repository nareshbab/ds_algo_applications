# Listing all the operations supported by Python data structures

"""
LIST
"""
sample = ["1", "2", "3", "4", "5"]

"""
[Needs argument]
Append adds an element at the end
['1', '2', '3', '4', '5', '6']
"""
sample.append("6")

"""
Pop removes an element at specific index or the last element of the list
pop without argument will remove '6'
pop with index will remove element at index 0

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
"""
sample.pop()
sample.pop(0)

"""
[Needs argument]
Index returns the index of the element
index('5') will give 4
"""
sample.index('5')

"""
[Needs argument]
Insert will add an element at specific index
insert(0, "abc") will add "abc" at the 0th index
"""
sample.insert(0, "abc")

"""
Sort the list in ascending order and return None.
        
The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.
"""
sample.sort()
sample.sort(key=max, reverse=True)

"""
[Needs argument]
Counts the number of occurences of an element
>>> sample.count("5") -> 1
"""
sample.count("5")

"""
Clear removes all the elements from the list
"""
sample.clear()

"""
Copy returns a shallow copy of the original list
>>> s1 = [1,2,3,[1,2,3]]
>>> s2 = s1.copy()
>>> s2
>>> [1, 2, 3, [1, 2, 3]]
>>> s2.append(5)
>>> s1
>>> [1, 2, 3, [1, 2, 3]]
>>> s2
>>> [1, 2, 3, [1, 2, 3], 5]
>>> s2[3].append(4)
>>> s1
>>> [1, 2, 3, [1, 2, 3, 4]]
>>> s2
>>> [1, 2, 3, [1, 2, 3, 4], 5]
"""
sample.copy()

"""
[Needs argument]
Extends one list with another
>>> s1
>>> [1, 2, 3, [1, 2, 3, 4]]
>>> s1.extend([10,11,12])
>>> s1
>>> [1, 2, 3, [1, 2, 3, 4], 10, 11, 12]
"""
sample.extend([10, 11, 12])

"""
[Needs argument]
Removes first occurrence of the value 
>>> s1
>>> [1, 2, 3, [1, 2, 3, 4]]
>>> s1.remove(1)
>>> s1
>>> [2, 3, [1, 2, 3, 4], 10, 11, 12]
"""
sample.remove(1)

"""
Reverses the order of elements of a list
"""
sample.reverse()
