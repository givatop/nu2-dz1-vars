right_answers = {
    "Иосиф Сталин": 1878,
    "Владимир Высоцкий": 1938,
    "Виктор Цой": 1962,
    "Андрей Сахаров": 1921,
    "Юрий Гагарин": 1934,
}

user_answers = {
    "Иосиф Сталин": None,
    "Владимир Высоцкий": None,
    "Виктор Цой": None,
    "Андрей Сахаров": None,
    "Юрий Гагарин": None,
}

names_num = len(right_answers)

done = False
while not done:

    for name in user_answers.keys():
        user_answers[name] = int(input(f"В каком году родился {name}?\n"))

    right_answers_num = 0
    for (right_answer, user_answer) in zip(right_answers.values(), user_answers.values()):
        right_answers_num += int(right_answer == user_answer)

    wrong_answers_num = names_num - right_answers_num
    print(f'Верных ответов: {right_answers_num}')
    print(f'Неверных ответов: {wrong_answers_num}')
    print(f'% верных ответов: {(right_answers_num * 100) / names_num:.1f}%')
    print(f'% неверных ответов: {(wrong_answers_num * 100) / names_num:.1f}%')

    user_input = input("Начать с начала?\n")
    done = True if user_input.lower() == "нет" else False
