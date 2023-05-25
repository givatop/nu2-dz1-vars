pushkin_born_year = 1799
pushkin_born_day = 6
user_input = None


while user_input != pushkin_born_year:
    user_input = int(input("В каком году родился А.С. Пушкин?\n"))


user_input = None

while user_input != pushkin_born_day:
    user_input = int(input(f"Какого июня {pushkin_born_year} г. родился А.С. Пушкин?\n"))


print("Верно")
