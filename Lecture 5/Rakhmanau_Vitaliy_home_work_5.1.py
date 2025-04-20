# Необходимо создать функцию для определения года: висоскосный либо нет.

def is_year_leap(year):
 #   
 #
 #
 #

test_data = [1500, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]

for year, result in zip(test_data, test_results):
    if is_year_leap(year) == result:
        print(year, 'is leap? -->', result)
    else:
        print(year, 'from your func -->', \
              is_year_leap(year))
        print('but expected -->', result)