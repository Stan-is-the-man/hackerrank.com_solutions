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
