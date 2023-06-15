# alphabet_dict = {chr(97 + i): i + 1 for i in range(26)}
# print(alphabet_dict)
#
# b = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
#      'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
#      'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#      'z': 26}
#
# print(len(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
# ))
#
# import itertools
#
# letters = ['a', 'b', 'c', 'd']
# to_int = [ord(x) for x in letters]
# words = [''.join(str(x) for x in to_int) for num in itertools.permutations(to_int)]
# print(words)
# # print(to_int)
# a = ['cba', 'abc', 'acb', 'bac', 'bca', 'cab', ]
# a.sort()
# print(a)

a = 'abd'
b = list(a)
print(b)
