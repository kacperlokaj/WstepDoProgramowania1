def znaki(s):
    result = {}
    for char in s:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    return result
s = "znaki napisu"
chars = znaki(s)
print(chars)

for k in chars.keys(sorted()):
    print(k,cn[k])

