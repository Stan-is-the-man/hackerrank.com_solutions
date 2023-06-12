# Sort a list without a built in function
my_list = [4, 8, 5, 2, 2, -7]
sorted_list = []

while my_list:
    max_value = max(my_list)
    min_value = 0
    current_index = 0

    for x in range(len(my_list)):
        if my_list[x] < max_value:
            max_value = my_list[x]
            current_index = x

    min_value = max_value
    sorted_list.append(min_value)
    my_list.pop(current_index)

print(sorted_list)


##################################################

# Compressed string from HackerRank

def compressedstring(message):
    new_str = ''
    counter = 1
    last = False
    for x in range(len(message)):
        current = message[x]
        if x == len(message) - 1:
            if counter == 1:
                new_str += message[x]
            break
        elif message[x] == message[x + 1]:
            new_str += message[x]
            counter += 1
            if x == len(message) - 2:
                new_str += str(counter)
        elif message[x] != message[x + 1] and counter > 1:
            new_str += str(counter)
            counter = 1
        else:
            new_str += message[x]
    return new_str


print(compressedstring('abc'))
print(compressedstring('abaasass'))
################################################################

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n % 2 != 0 and n < 2:
    print("Weird")
elif n % 2 == 0 and (2 <= n <= 5):
    print("Not Weird")
elif n % 2 == 0 and (6 <= n <= 20):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")


################################################################

def plus_minus(arr):
    positive = 0
    negative = 0
    zeroes = 0

    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zeroes += 1
    print(f'{positive / len(arr):6f}\n{negative / len(arr):6f}\n{zeroes / len(arr):6f}\n')


print(plus_minus([1, 1, 0, -1, -1]))


################################

def staircase(n):
    result = ''
    for x in range(n):
        result += (n - x - 1) * ' '
        if x == n - 1:
            result += (x + 1) * '*'
        else:
            result += (x + 1) * '*' + '\n'
    print(result)


################################

def birthdayCakeCandles(candles: list):
    max_candle_size = max(candles)
    count_of_max_sized_candles = 0
    for candle in candles:
        if candle == max_candle_size:
            count_of_max_sized_candles += 1

    return count_of_max_sized_candles


print(birthdayCakeCandles([3, 2, 1, 3]))


################################

def time_conversion(s: str):
    result = ''
    to_24_dict = {
        '01': '13', '02': '14', '03': '15', '04': '16',
        '05': '17', '06': '18', '07': '19', '08': '20',
        '09': '21', '10': '22', '11': '23',
        '12': '12'
    }

    hours = s[0:2]
    if s[-2] == "P":
        result += to_24_dict[hours]
        result += s[2:8]
        return result
    if s[-2] == 'A':
        if hours == '12':
            hours = '00'
        res = hours + s[2:8]
        return res


print(time_conversion('12:45:00AM'))


################################
# student grades

def grading_students(grades):
    new_grades = []

    for num in grades:
        if num < 38:
            new_grades.append(num)
        else:
            for x in range(num, num + 5):
                if x % 5 == 0 and (x - num) < 3:
                    new_grades.append(x)
                    break
                if x % 5 == 0 and (x - num) >= 3:
                    new_grades.append(num)
                    break

    return new_grades


print(grading_students([73, 67, 38, 33]))
################################################################
