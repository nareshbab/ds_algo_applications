# Listing all the operations supported by Python data structures

"""
SET
NOTE: to create an empty set you have to use set(), not {};
the latter creates an empty dictionary, a data structure
that we discuss in the next section.
"""
sample = {"a", "c"}  # set literal, similar to set(["a", "c"])
sample2 = set()  # creates an empty set
sample3 = {}  # creates an empty dictionary and not set
s1 = set('abracadabra')  # {'b', 'd', 'c', 'a', 'r'}

"""
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
"""

"""
[Needs argument]
Adds an element to the set
>>> s1.add(3)
>>> s1
{3, 4, 6, 7}
"""
sample.add("8")

"""
Update adds list of elements to sets
IMP:: Nested list in update method is not supported
>>> s1 = {1,2,3}
>>> s1.update()
>>> s1
{1, 2, 3}
>>> s1.update(4)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'int' object is not iterable
>>> s1.update([4])
>>> s1
{1, 2, 3, 4}
>>> s1.update([4,5])
>>> s1
{1, 2, 3, 4, 5}
>>> s1.update([4,5, [1,2,3]])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
"""
sample.update(["88"])

"""
[Needs argument]
Copy creates a shallow copy of the set
"""
sample.copy()

"""
[Cannot pass arguments]
Pop removes an element from the start of set
>>> s1
{1, 2, 3, 4, 5}
>>> s1.pop()
1
>>> s1
{2, 3, 4, 5}
>>> s1.pop()
2
>>> s1
{3, 4, 5}
"""
sample.pop()

"""
Clear removes all the elements from set
>>> s1
{3, 4, 5}
>>> s1.clear()
>>> s1
set()
"""
sample.clear()

"""
[Needs argument]
Removes an element from the set
IMP:: remove raises a KeyError if key not present
	  discard will not raise any KeyError
>>> s1
{2, 3, 4, 5, 6, 7}
>>> s1.remove(2)
>>> s1
{3, 4, 5, 6, 7}
>>> s1.remove(5)
>>> s1.remove(9)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 9
>>> s1.discard(9)
"""
sample.remove("9")

"""
[Needs argument]
Difference returns the difference of two sets 
i.e all elements in s1 but not in s2
>>> s1 = {1, 2, 3}
>>> s1.difference()
{1, 2, 3}
>>> s2 = {3, 4, 5}
>>> s1.difference(s2)
{1, 2}
>>> s1 - s2
{1, 2}
>>> s1.difference_update(s2)
>>> s1
{1, 2}
"""
sample.difference(sample2)

"""
[Needs argument]
Difference update calculates the difference and updates the source set
i.e all elements in s1 but not in s2
>>> s1 = {1, 2, 3}
>>> s1.difference()
{1, 2, 3}
>>> s2 = {3, 4, 5}
>>> s1.difference(s2)
{1, 2}
>>> s1
{1, 2, 3}
>>> s1 - s2
{1, 2}
>>> s1.difference_update(s2)
>>> s1
{1, 2}
"""
sample.difference_update()

"""
[Needs argument]
Removes an element from the set
IMP:: remove raises a KeyError if key not present
	  discard will not raise any KeyError
>>> s1
{3, 4, 6, 7}
>>> s1.remove(9)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
KeyError: 9
>>> s1.discard(9)
>>> s1.discard(7)
>>> s1
{3, 4, 6}
"""
sample.discard("10")

"""
[Needs argument]
Intersection will return a set of elements present in both the sets
>>> s1
{3, 4, 6}
>>> s2 = {4,6,7}
>>> s1.intersection(s2)
{4, 6}
>>> s1
{3, 4, 6}
>>> s1.intersection_update(s2)
>>> s1
{4, 6}
"""
sample.intersection()

"""
[Needs argument]
Intersection will return a set of elements present in both the sets
>>> s1
{3, 4, 6}
>>> s2 = {4,6,7}
>>> s1.intersection(s2)
{4, 6}
>>> s1
{3, 4, 6}
>>> s1.intersection_update(s2)
>>> s1
{4, 6}
"""
sample.intersection_update()

"""
[Needs argument]
Disjoint will return True if no element is common between two sets
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.isdisjoint(s2)
False
>>> s1.isdisjoint({7,8,9})
True
"""
sample.isdisjoint(sample2)

"""
[Needs argument]
Returns True if source set is subset of another set
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.issubset(s2)
True
>>> s1.issuperset(s2)
False
"""
sample.issubset()

"""
[Needs argument]
Returns True if source set is superset of another set
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.issubset(s2)
True
>>> s1.issuperset(s2)
False
"""
sample.issuperset()

"""
[Needs argument]
[Needs argument]
Return the symmetric difference of two sets as a new set.
(i.e. all elements that are in exactly one of the sets.)
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.symmetric_difference(s2)
{7}
>>> s1.symmetric_difference_update(s2)
>>> s1
{7}
"""
sample.symmetric_difference(sample2)

"""
[Needs argument]
Return the symmetric difference of two sets as a new set.
(i.e. all elements that are in exactly one of the sets.)
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.symmetric_difference(s2)
{7}
>>> s1.symmetric_difference_update(s2)
>>> s1
{7}
"""
sample.symmetric_difference_update(sample2)

"""
[Needs argument]
Union returns a new set with all the elements in either of the set
>>> s1
{4, 6}
>>> s2
{4, 6, 7}
>>> s1.union(s2)
{4, 6, 7}
"""
sample.union()
