def remove_duplicate(s):
    result=""
    for ch in s:
        if ch not in result:
            result +=ch
    return result
print(remove_duplicate("programming"))

#Replace space with %20(asked in google)
s=("hello world python")
o/p:
hello%20world%python