import sqlite3
from pathlib import Path
from sqlite3 import Connection

from modules.my_models import Answer, Question, Student, Theme


class MyDatabase:
    """Класс по работе с базой данных"""

    def __init__(self):
        """Инициализация класса"""
        self.conn: Connection | None = None

        if self.__connect_to_db():
            print("БД подключена успешно!")
        else:
            print("БД ошибка подключения!")



    def __connect_to_db(self) -> bool:
        """Метод по подключению к базе данных

        Returns:
            bool: True, если успешно
        """
        # путь к файлу с базой данных
        path_db = Path(__file__).parent.parent.resolve() / "my_database.db"
        # проверяем, есть ли файл базы данных
        if path_db.exists():
            self.conn = sqlite3.connect(path_db)
        else:
            # если файла нет, создать его
            self.conn = sqlite3.connect(path_db)
            # создать таблицы
            self.__create_students_table()
            self.__create_themes_table()
            self.__create_questions_table()
            self.__create_answers_table()
            # наполнить таблицы данными
            self.__fill_students_table()
            self.__fill_other_tables()

        return bool(self.conn)



    def __create_students_table(self):
        """Метод по созданию таблицы с учениками
        """
        # проверка на наличие соединения
        assert self.conn, "Соединение не установлено"

        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            age INT NOT NULL,
            grade TEXT NOT NULL
            );
        ''')


    def __create_themes_table(self):
        """Метод по созданию таблицы с темами для тестов
        """
        # проверка на наличие соединения
        assert self.conn, "Соединение не установлено"

        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS themes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
            );
        ''')


    def __create_questions_table(self):
        """Метод по созданию таблицы с вопросами
        """
        # проверка на наличие соединения
        assert self.conn, "Соединение не установлено"

        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            theme_id INTEGER NOT NULL,
            FOREIGN KEY (theme_id) REFERENCES themes(id)
            );
        ''')


    def __create_answers_table(self):
        """Метод по созданию таблицы с вариантами ответов на вопросы
        """
        # проверка на наличие соединения
        assert self.conn, "Соединение не установлено"

        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            is_valid INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id)
            );
        ''')


    def __fill_students_table(self):
        """Метод для заполнения таблицы с данными учащихся
        """
        # проверка наличия соединения
        assert self.conn, "Соединение не установлено"

        cur = self.conn.cursor()
        # формируем список из кортежей с учениками
        data = [
            ("Иванов", "Иван", 16, "10А"),
            ("Сидоров", "Сидор", 15, "9В"),
            ("Петров", "Петр", 16, "10Б"),
        ]
        # выполняем множественную вставку данных в таблицу students
        cur.executemany("INSERT INTO students(last_name, first_name, age, grade) VALUES (?, ?, ?, ?);", data)
        self.conn.commit()


    def __fill_other_tables(self):
        """Метод по заполнению оставшихся таблиц
        """
        # проверка наличия соединения
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()

        # Темы
        themes_data = [
            ("История",),
            ("География",),
            ("Информатика",),
        ]
        # Осуществить вставку тем
        cur.executemany("INSERT INTO themes(name) VALUES (?)", themes_data)
        self.conn.commit()

        # Вопросы
        questions_data = [
            ("В каком году произошло Крещение Руси князем Владимиром Святославичем?", 1),
            ("Когда состоялась Невская битва, в которой новгородский князь Александр Ярославич разбил шведов?", 1),
            ("В каком году произошла Куликовская битва, ставшая важным шагом на пути к освобождению от ордынского ига?", 1),
            ("В каком году Иван IV (Грозный) венчался на царство и стал первым русским царём?", 1),
            ("Когда народное ополчение под предводительством Кузьмы Минина и Дмитрия Пожарского освободило Москву от польских интервентов?", 1),
            ("В каком году Пётр I основал город Санкт-Петербург?", 1),
            ("В каком году состоялось Бородинское сражение в ходе Отечественной войны против армии Наполеона?", 1),
            ("Когда император Александр II подписал Манифест об отмене крепостного права в России?", 1),
            ("В каком году началась и закончилась Великая Отечественная война?", 1),
            ("Когда Юрий Гагарин совершил первый в истории человечества полёт в космос?", 1),
        ]
        cur.executemany("INSERT INTO questions(question, theme_id) VALUES (?, ?)", questions_data)
        self.conn.commit()

        # Ответы
        answers_data = [
            ("988 год", 1, 1), ("896 год", 1, 0), ("786 год", 1, 0),
            ("15 июля 1240 года", 2, 1), ("11 декабря 1238 года", 2, 0), ("14 июня 1239 года", 2, 0),
            ("8 сентября 1380 года", 3, 1), ("2 января 1350 года", 3, 0), ("4 июня 1349 года", 3, 0),
            ("1547 год", 4, 1), ("1567 год", 4, 0), ("1789 год", 4, 0),
            ("1612 год", 5, 1), ("1589 год", 5, 0), ("1590 год", 5, 0),
            ("1703 год", 6, 1), ("1689 год", 6, 0), ("1749 год", 6, 0),
            ("1812 год", 7, 1), ("1868 год", 7, 0), ("1799 год", 7, 0),
            ("1861 год", 8, 1), ("1855 год", 8, 0), ("1847 год", 8, 0),
            ("1941–1945 годы", 9, 1), ("1955–1969 годы", 9, 0), ("1943–1955 годы", 9, 0),
            ("12 апреля 1961 года", 10, 1), ("2 февраля 1956 года", 10, 0), ("4 марта 1947 года", 10, 0),
        ]
        cur.executemany("INSERT INTO answers(answer, question_id, is_valid) VALUES (?, ?, ?)", answers_data)
        self.conn.commit()


    def get_students(self) -> list[Student]:
        """Метод получения всего списка учащихся

        Returns:
            list[Student]: список учащихся
        """
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()
        cur.row_factory = sqlite3.Row
        # получаем данные о студентах из базы данных
        cur.execute("SELECT id, last_name, first_name, age, grade FROM students")
        student_data = cur.fetchall()
        # преобразуем их в объекты класса Student и возвращаем списком
        return [Student(**student) for student in student_data]


    def get_themes(self) -> list[Theme]:
        """Метод получения списка тем

        Returns:
            list[Theme]: список тем
        """
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()
        cur.row_factory = sqlite3.Row
        # получаем данные о темах из базы данных
        cur.execute("SELECT id, name FROM themes")
        themes_data = cur.fetchall()
        # преобразуем их в объекты класса Student и возвращаем списком
        return [Theme(**theme) for theme in themes_data]


    def get_questions(self, theme_id: int) -> list[Question]:
        """Метод получения списка вопросов по выбранной теме

        Args:
            theme_id (int): идентификатор темы

        Returns:
            list[Question]: список вопросов
        """
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()
        cur.row_factory = sqlite3.Row
        # получение вопросов по выбранной теме
        cur.execute("SELECT id, question, theme_id FROM questions WHERE theme_id=?", (theme_id,))
        questions_data = cur.fetchall()
        return [Question(**question) for question in questions_data]


    def get_answers(self, question_id: int) -> list[Answer]:
        """Метод получения списка вариантов ответов

        Args:
            question_id (int): идентификатор вопроса

        Returns:
            list[Answer]: список вариантов ответов
        """
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()
        cur.row_factory = sqlite3.Row
        # получение списка вариантов ответов по выбранному вопросу
        cur.execute("SELECT id, answer, question_id, is_valid FROM answers WHERE question_id=?", (question_id,))
        answers_data = cur.fetchall()
        return [Answer(**answer) for answer in answers_data]

    def check_answer(self, answer_id: int) -> bool:
        """Метод проверки ответа

        Args:
            answer_id (int): идентификатор ответа

        Returns:
            bool: если верно, то истинно
        """
        assert self.conn, "Соединение не установлено"
        cur = self.conn.cursor()
        cur.row_factory = sqlite3.Row
        # получаем ответ, который выбрал пользователь
        cur.execute("SELECT id, answer, question_id, is_valid FROM answers WHERE id=?", (answer_id,))
        answer: Answer = Answer(**cur.fetchone())
        # проверяем верный(1) он или нет(0)
        if answer.is_valid == 1:
            return True
        else:
            return False