# Listing all the operations supported by Python data structures

"""
DICT
"""
sample = {"a": 1, "b":2, "c":3}

"""
[Needs argument]
Pop removes a key from the dict and returns the value of that key
>>> sample = {"a": 1, "b":2, "c":3}
>>> sample.pop("a")
1
"""
sample.pop("a")

"""
[Cannot pass argument]
Popitem removes the last key from the dict
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
>>> s2.popitem()
('n', 22)
>>> s2.popitem()
('e', 5)
>>> s2.popitem("a")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: dict.popitem() takes no arguments (1 given)
"""
sample.popitem()

"""
Copy creates a shallow copy of the original dict
>>> s1 = {"a": 1, "b":2, "c":3}
>>> s2 = s1
>>> s2.update({"d": 4})
>>> s2
>>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> s1
>>> {'a': 1, 'b': 2, 'c': 3, 'd': 4}

>>> s1 = {"a": 1, "b":2, "c":3, "d": [1,2,3]}
>>> s2 = s1.copy()
>>> s2.update({"e": 5})
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3], 'e': 5}
>>> s1
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}
>>> s2["d"].append(4)
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5}
>>> s1
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4]}
"""
sample.copy()

"""
Clear removes all the keys from the dict
"""
sample.clear()

"""
Items returns an iterable list of tuples with key and value
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5}
>>> s2.items()
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', [1, 2, 3, 4]), ('e', 5)])
>>> for k,v in s2.items():
>>> 	print(k, v)
a 1
b 2
c 3
d [1, 2, 3, 4]
e 5
"""
sample.items()

"""
[Needs argument]
Insert key with a value of default if key is not in the dictionary.
Return the value for key if key is in the dictionary, else default.
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5}
>>> s2.setdefault("n", 33)
33
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 33}
>>> s2.setdefault("e", 33)
5
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 33}
>>> s2["n"] = 22
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
"""
sample.setdefault("n", 33)

"""
[Needs argument]
Values return the list of values of all the keys
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
>>> s2.values()
dict_values([1, 2, 3, [1, 2, 3, 4], 5, 22])
"""
sample.values()

"""
[Needs argument]
Create a new dictionary with keys from iterable and values set to value
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
>>> s2.fromkeys("a", "b", "c")
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: fromkeys expected at most 2 arguments, got 3
>>> s2.fromkeys("a", "b")
{'a': 'b'}
>>> s2.fromkeys(["a"])
{'a': None}
>>> s2.fromkeys(["a", "b"])
{'a': None, 'b': None}
>>> s2.fromkeys(["a", "b"], [1,2])
{'a': [1, 2], 'b': [1, 2]}
>>> s2.fromkeys(["a", "b"], [1,2], [1,2])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: fromkeys expected at most 2 arguments, got 3
"""
sample.fromkeys(["a"], 2)

"""
[Needs argument]
Get returns the key value if key is present otherwise default value
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
>>> s2.get('b')
2
>>> s2.get('k')
>>> s2.get('k', None)
>>> s2.get('k', 5)
5
"""
sample.get("k", "default_value")

"""
Keys returns an iterable of all the keys in the dictionary
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'e': 5, 'n': 22}
>>> s2.keys()
dict_keys(['a', 'b', 'c', 'd', 'e', 'n'])
"""
sample.keys()

"""
Update merges two dicts
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4]}
>>> s2.update()
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4]}
>>> s2.update({"k":33, "m":44})
>>> s2
{'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4], 'k': 33, 'm': 44}
"""
sample.update()