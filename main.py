# factor of number
def get_totalX(a, b):
    count = 0
    max_a = max(a)
    min_b = min(b)

    # Check each integer between the two arrays
    for num in range(max_a, min_b + 1):
        if all(num % x == 0 for x in a) and all(y % num == 0 for y in b):
            count += 1

    return count


print(get_totalX([2, 6], [24, 36]))
