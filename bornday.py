import sys


pushkin_born_year = 1799
pushkin_born_day = 6

user_input = int(input("В каком году родился А.С. Пушкин?\n"))

if user_input != pushkin_born_year:
    print("Неверный год рождения")
    sys.exit()

user_input = int(input(f"Какого июня {pushkin_born_year} г. родился А.С. Пушкин?\n"))

if user_input != pushkin_born_day:
    print("Неверный день рождения")
    sys.exit()

print("Верно")
