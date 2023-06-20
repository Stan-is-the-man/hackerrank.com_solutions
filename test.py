def at_least_1_uppercase(password):
    for char in password:
        if 65 <= ord(char) <= 90:
            return True


print(at_least_1_uppercase('b'))
