#most frquent character
def maxchar_frequency(s):
    freq={}
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    return max(freq,key=freq.get)
print(maxchar_frequency("bannana"))