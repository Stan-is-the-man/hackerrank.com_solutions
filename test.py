s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'
chars = {}

for char in s:
    if char not in chars:
        chars[char] = 0
    chars[char] += 1
new_str = ''

for k, v in chars.items():
    if v % 2 == 1:
        new_str += k
print(chars)
print(new_str)
