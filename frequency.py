def char-frequency(s):
    freq={}
    for ch in s:
            freq[ch]=freq.get(ch,0)+1
 return freq
print(char-frequency("aabbcc")