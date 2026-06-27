#Using counter
from collections import counter
def first_unique(s):
    freq=counter(s)
    for ch in s:
        if freq[ch]==1:
            return ch
        return None
print(first_unique("aabbcdde"))