from pathlib import Path

import sqlite3
from sqlite3 import Connection

class MyDatabase:
    """Класс по работе с базой данных"""

    def __init__(self):
        """Инициализация класса"""
        self.conn: Connection  = None

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
        self.conn: Connection = sqlite3.connect(path_db)
        if self.conn:
            return True
        return False


    def _create_students_table(self):
        """Метод по созданию таблицы с учениками

        Returns:
            bool: True, если успешно
        """
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

        Returns:
            bool: True, если успешно
        """
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS themes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
            );
        ''')


    def _create_questions_table(self):
        """Метод по созданию таблицы с вопросами

        Returns:
            bool: True, если успешно
        """
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

        Returns:
            bool: True, если успешно
        """
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id)
            );
        ''')