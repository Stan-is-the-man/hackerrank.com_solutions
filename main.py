def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return 'YES'

    if (x1 < x2 and v1 <= v2) or (x1 > x2 and v1 >= v2):
        return 'NO'

    # return "YES"

    current_position_x1 = x1
    current_position_x2 = x2

    while True:
        current_position_x1 += v1
        current_position_x2 += v2

        if current_position_x1 == current_position_x2:
            return 'YES'
        if current_position_x1 > current_position_x2:
            return 'NO'


print(kangaroo(21, 6, 47, 3))
