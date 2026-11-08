import sqlite3
from pathlib import Path
from sqlite3 import Connection


class MyDatabase:
    """Класс по работе с базой данных"""

    def __init__(self):
        """Инициализация класса"""
        self.conn: Connection | None = None

        if self.connect_to_db():
            print("БД подключена успешно!")
        else:
            print("БД ошибка подключения!")
        self._create_students_table()
        self._create_themes_table()
        self._create_questions_table()
        self._create_answers_table()


    def connect_to_db(self) -> bool:
        """Метод по подключению к базе данных

        Returns:
            bool: True, если успешно
        """
        # путь к файлу с базой данных
        path_db = Path(__file__).parent.parent.resolve() / "my_database.db"
        # TODO продумать, как сделать, если файла с БД нет, то создать его и наполнить таблицами, и данными,
        #  если же файл с БД есть - то просто соединиться с ней
        self.conn = sqlite3.connect(path_db)
        # Если соединение есть, вернет True
        return bool(self.conn)


    def _create_students_table(self):
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


    def _create_themes_table(self):
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


    def _create_questions_table(self):
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


    def _create_answers_table(self):
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
            FOREIGN KEY (question_id) REFERENCES questions(id)
            );
        ''')


    def fill_students_table(self):
        """Заполнить таблицу данными учащихся
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


    def fill_other_tables(self):
        """Заполнить оставшиеся таблицы
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
        # questions_data = [
        #   ...
        # ]
        # cur.executemany(...)
        # self.conn.commit()

        # Ответы
        # answers_data = [
        #    ...
        # ]
        # cur...
        # self...
        # TODO доделать данный метод, чтобы заполнялись оставшиеся
        #  таблицы с учетом связей по внешнему ключу