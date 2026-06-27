def count_vowels_consonants(s):
    vowels="aeiouAEIOU"
    v=c=0
    for ch in s:
        if ch.isalpha():
            v+=1
    else:
        c+=1
    return v,c
print(count_vowels_consonants("python programming"))