def longest_subarray(arr):
    # arr.sort()
    longest_length = 0
    current_length = 1

    for x in range(1, len(arr)):
        curr = arr[x]
        if arr[x] - arr[x - 1] <= 1:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 1  # Reset the length for the new subarray

    longest_length = max(longest_length, current_length)

    return longest_length


print(longest_subarray([4, 6, 5, 3, 3, 1]))
