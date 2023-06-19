def square_is_magic(square):
    n = len(square)
    magic_sum = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != magic_sum:
            return False

    # Check columns
    for x in range(n):
        column_sum = sum(square[z][x] for z in range(n))
        if column_sum != magic_sum:
            return False

    # Check main diagonal
    diagonal_sum = sum(square[i][i] for i in range(n))
    if diagonal_sum != magic_sum:
        return False

    # Check secondary diagonal
    secondary_diagonal_sum = sum(square[i][n - i - 1] for i in range(n))
    if secondary_diagonal_sum != magic_sum:
        return False

    return True


print(square_is_magic([[8, 3, 4], [1, 5, 9], [6, 7, 2]]))


def forming_magic_square(s):
    pass
