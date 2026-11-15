from modules.my_database import MyDatabase

db: MyDatabase = MyDatabase()

# получение списка учащихся
students = db.get_students()
# вывод списка учащихся пользователю
for student in students:
    print(student.id, student.first_name, student.last_name, student.grade)
# сохраняем выбранного учащегося
student_id = int(input("Введите айди студента = "))

# получение списка тем
themes = db.get_themes()
# вывод списка тем пользователю
for theme in themes:
    print(theme.id, theme.name)
# сохраняем выбранную тему
theme_id = int(input("Введите айти темы = "))

# получение списка ответов
questions = db.get_questions(theme_id)
# вывод списка вопросов пользователю
for question in questions:
    print(question.question)
    # получение списка ответов к текущему вопросу
    answers = db.get_answers(question.id)
    # вывод списка ответов
    for answer in answers:
        print(answer.id, answer.answer)
    # получаем ответ на вопрос
    answer_id = int(input("Выбери айди ответа = "))
    # проверяем верность ответа
    if db.check_answer(answer_id):
        print("Верно")
    else:
        print("Неверно!")