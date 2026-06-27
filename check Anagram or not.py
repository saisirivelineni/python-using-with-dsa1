def is_anagram(s1, s2):
    return sorted(s1)==sorted(s2)
print(is_anagram("listen","silent"))


from collections import Counter
def is_anaragram (s1,s2):
   return  Counter (s1)