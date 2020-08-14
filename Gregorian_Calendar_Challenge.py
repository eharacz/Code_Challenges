## Gregorgian Leap Year Calendar ##


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print(True)
    elif year % 400 == 0:
        print(True)
    else:
        print(False)


leap_year(1990)
leap_year(2000)
leap_year(2400)
leap_year(1800)
leap_year(1900)
leap_year(2100)
leap_year(2200)
leap_year(2300)
leap_year(2500)
leap_year(2004)
