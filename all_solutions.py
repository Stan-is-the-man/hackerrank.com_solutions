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

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    apples_on_target = 0
    oranges_on_target = 0

    for apple in apples:
        if s <= (a + apple) <= t:
            apples_on_target += 1

    for oranges in oranges:
        if s <= (b + oranges) <= t:
            oranges_on_target += 1
    return f'{apples_on_target}\n{oranges_on_target}'


print(count_apples_and_oranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]))


################################
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


#########################################################

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


###############
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
###############

# Comprehension vs map

# map
cores_map = list(map(int, input().rstrip().split()))
# list comprehension
cores_compr = [int(x) for x in input().strip().split()]


################################
def breaking_records(scores):
    max_score = scores[0]
    min_score = scores[0]
    update_counter = [0, 0]

    for x in range(1, len(scores)):
        if scores[x] > max_score:
            max_score = scores[x]
            update_counter[0] += 1
        elif scores[x] < min_score:
            min_score = scores[x]
            update_counter[1] += 1

    return update_counter


print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))


################################################################
def mini_max_sum(arr):
    new_arr = []
    arr.sort()
    new_arr.append(sum(arr[0:4]))
    new_arr.append(sum(arr[1:5]))

    return ' '.join(str(x) for x in new_arr)


print(mini_max_sum([1, 3, 5, 7, 9]))


################################################################
def birthday(s, d, m):
    if len(s) == 1 and s[0] == d:
        return 1
    number_of_ways_bar_can_be_divided = 0
    for x in range(len(s) - m + 1):
        current_sum = 0
        for z in range(x, x + m):
            current_sum += s[z]
        if current_sum == d:
            number_of_ways_bar_can_be_divided += 1

    return number_of_ways_bar_can_be_divided


print(birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7))


################################
def migratory_birds(arr):
    types = {}
    for num in arr:
        if num not in types:
            types[num] = 0
        types[num] += 1

    max_frequency = max(types.values())
    keys_with_max_frequency = []
    for k, v in types.items():
        if v == max_frequency:
            keys_with_max_frequency.append(k)
    keys_with_max_frequency.sort()
    return keys_with_max_frequency[0]


print(migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))


################################################################
# julian and gregorian calendars
def day_of_programmer(year):
    days_of_first_8_moths = 243

    if year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        days_of_first_8_moths += 1
    elif year == 1918:
        days_of_first_8_moths -= 13
    elif year < 1918 and year % 4 == 0:
        days_of_first_8_moths += 1

    the_day_of_programmer = 256 - days_of_first_8_moths

    if len(str(the_day_of_programmer)) == 1:
        return f'0{the_day_of_programmer}.09.{year}'
    return f'{the_day_of_programmer}.09.{year}'


print(day_of_programmer(1918))


################################################################

# julian and gregorian calendars with functions

def is_leap_gregorian(year):
    if year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        return True


def is_leap_julian(year):
    if year < 1918 and year % 4 == 0:
        return True


def day_of_programmer(year):
    days_of_first_8_moths = 243

    if is_leap_gregorian(year) or is_leap_julian(year):
        days_of_first_8_moths += 1

    elif year == 1918:
        days_of_first_8_moths -= 13

    the_day_of_programmer = 256 - days_of_first_8_moths

    if len(str(the_day_of_programmer)) == 1:
        return f'0{the_day_of_programmer}.09.{year}'
    return f'{the_day_of_programmer}.09.{year}'


print(day_of_programmer(2016))


################################
def bon_appetit(bill, k, b):
    actual_bill = (sum(bill) - bill[k]) // 2
    if actual_bill < b:
        return b - actual_bill

    else:
        return 'Bon Appetit'


print(bon_appetit([3, 10, 2, 9], 1, 12))
################################################################
import itertools


def bigger_is_greater(w):
    greater_strings = []
    letters = [str(x) for x in w]
    words = [''.join(perm) for perm in itertools.permutations(letters)]

    for word in words:
        if word > w:
            greater_strings.append(word)
    greater_strings.sort()
    if greater_strings:
        return greater_strings[0]
    return 'no answer'


print(bigger_is_greater('zedawdm'))


################################
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


################################################################
def start_from_first_page(n, p):
    if p <= n / 2:
        return True


def zero_turns_start_from_first(n, p):
    if p == n or p == 0:
        return True


def zero_turns_start_from_last(n, p):
    if (n % 2 != 0) and (n == p or p == n - 1):
        return True


def page_count(n, p):
    turns = 0
    if start_from_first_page(n, p):
        if zero_turns_start_from_first(n, p):
            return 0

        left = 0
        right = 1
        while left != p and right != p:
            left += 2
            right += 2
            turns += 1

    else:
        if zero_turns_start_from_last(n, p):
            return 0

        if n % 2 == 0:
            left = n
            right = n + 1
        else:
            left = n
            right = n - 1
        while left != p and right != p:
            left -= 2
            right -= 2
            turns += 1

    return turns


print(page_count(7, 4))


################################################################
def counting_valleys(steps, path):
    number_of_valleys_walked_through = 0
    current_level = 0
    for step in path:
        if current_level == 0 and step == 'D':
            number_of_valleys_walked_through += 1
        if step == 'U':
            current_level += 1
        else:
            current_level -= 1
    return number_of_valleys_walked_through


print(counting_valleys(8, 'UDDDUDUU'))


################################################################
def get_money_spent(keyboards, drives, b):
    current_max_sum_in_the_budget = 0

    for x in range(len(keyboards)):
        for z in range(len(drives)):
            if b >= keyboards[x] + drives[z] > current_max_sum_in_the_budget:
                current_max_sum_in_the_budget = keyboards[x] + drives[z]
    if current_max_sum_in_the_budget != 0:
        return current_max_sum_in_the_budget

    return -1


print(get_money_spent([5], [4], 5))
################################################################
# всяко с всяко от лист
# first element with every other elements from a list
from collections import deque


def longest_subarray(a):
    if min(a) == max(a):
        return len(a)
    to_deque = deque(a)
    longest_run = 0
    for _ in range(len(to_deque)):
        current_array = list()
        current_array.append(to_deque[0])
        for z in range(1, len(to_deque) - 1):
            if abs(to_deque[0] - to_deque[z]) <= 1:
                current_array.append(to_deque[z])

        smaller = []
        bigger = []
        for y in current_array:
            if to_deque[0] <= y:
                smaller.append(y)
            if to_deque[0] >= y:
                bigger.append(y)
        current_longest_run = max(len(smaller), len(bigger))
        if current_longest_run > longest_run:
            longest_run = current_longest_run
        to_deque.append(to_deque.popleft())

    return longest_run


print(longest_subarray([4, 6, 5, 3, 3, 1]))
print(longest_subarray([1, 1, 2, 2, 4, 4, 5, 5, 5]))
print(longest_subarray([1, 2, 2, 3, 1, 2]))
print(longest_subarray([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]))
############################################
# def at_least_6_length(password):
#     if len(password) >= 6:
#         return True


def at_least_1_digit(password):
    for char in password:
        if char.isdigit():
            return True


def at_least_1_lowercase(password):
    for char in password:
        if char.islower():
            return True


def at_least_1_uppercase(password):
    for char in password:
        if char.isupper():
            return True


def has_special_character(password):
    for char in password:
        if char in ['!', '@', '#', '$', '%', '^', '(', ')', '-', '+']:
            return True


def minimum_number(n, password):
    conditions_not_considered = 0

    if not at_least_1_digit(password):
        conditions_not_considered += 1
    if not at_least_1_lowercase(password):
        conditions_not_considered += 1
    if not at_least_1_uppercase(password):
        conditions_not_considered += 1
    if not has_special_character(password):
        conditions_not_considered += 1

    if n + conditions_not_considered >= 6 or n >= 6:
        return conditions_not_considered

    return 6 - n


print(
    minimum_number
    (10,'e+*@f%@e^)!@$ctv!*s&-#$*%j^(&@u$vu)&rr^dhi!)sc(une@#s%x!#%*wz+ew#k@k^%(j@-w^$^(vhjy(#!z@d+)d*+b@#a^#'))
#################################
def bigSorting(unsorted):
    int_list = [int(x) for x in unsorted]
    int_list.sort()
    return '\n'.join(str(x) for x in int_list)


print(bigSorting(['5', '1', '1232142323535']))
################################################################
#alphabet dict

import string

alphabet_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, 0)}
print(alphabet_dict)

#######################3
import string


def designer_pdf_viewer(h, word):
    alphabet_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, 0)}
    heights_of_the_word = []
    for char in word:
        heights_of_the_word.append(h[alphabet_dict[char]])
    return len(word) * max(heights_of_the_word)


print(designer_pdf_viewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'abc'))
########################################################################
def utopian_tree(n):
    initial_height = 1
    if n == 0:
        return initial_height
    for x in range(1, n + 1):
        if x % 2 != 0:
            initial_height *= 2
        else:
            initial_height += 1

    return initial_height


print(utopian_tree(4))
########################################################################################
def angryProfessor(k, a):
    on_time_students = 0
    for time in a:
        if time <= 0:
            on_time_students += 1
    if on_time_students < k:
        return 'YES'
    return 'NO'


print(angryProfessor(2, [0, -1, 2, 1]))
########################################

def hurdle_race(k, height):
    needed = max(height) - k
    if needed > 0:
        return needed
    return 0


print(hurdle_race(4, [1, 6, 3, 5, 2]))
########################################
def flatland_space_stations(n, c):
    all_max_distances = {0}

    for city_index in range(n):
        if city_index not in c:
            current_distances = []
            for space_station in c:
                current_distances.append(abs(space_station - city_index))
            all_max_distances.add(min(current_distances))

    return max(all_max_distances)


print(flatland_space_stations(6, [0, 1, 2, 4, 3, 5]))
################################
def beautiful_days(i, j, k):
    happy_days = 0

    for day in range(i, j + 1):
        d_str = str(day)
        d_rev_str = d_str[::-1]
        d_rev = d_rev_str.lstrip('0')
        if (abs(day - int(d_rev))) % k == 0:
            happy_days += 1

    return happy_days


print(beautiful_days(20, 23, 6))
