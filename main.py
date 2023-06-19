def super_reduced_string(s):
    for char in s:
        s = s.replace(char + char, "")

    return s if s else "Empty String"


print(super_reduced_string('aaabbaac'))
