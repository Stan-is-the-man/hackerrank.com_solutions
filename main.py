def divisible_sum_pairs(n, k, ar):
    number_of_pairs = 0
    ar.sort()
    for x in range(n - 1):
        for z in range(1, n - x):
            a = ar[x] + ar[x + z]
            if a % k == 0:
                number_of_pairs += 1
    return number_of_pairs


print(divisible_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6]))
