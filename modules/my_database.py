class MyDatabase:
    """Класс по работе с базой данных"""

    def __init__(self):
        """Инициализация класса"""
        self.conn = None


    def connect_to_db(self) -> bool:
        """Метод по подключению к базе данных

        Returns:
            bool: True, если успешно
        """
        # TODO реализовать подключение к базе данных
        return False


    def _create_students_table(self) -> bool:
        """Метод по созданию таблицы с учениками

        Returns:
            bool: True, если успешно
        """
        # TODO реализовать создание таблицы с учениками
        return False


    def _create_themes_table(self) -> bool:
        """Метод по созданию таблицы с темами для тестов

        Returns:
            bool: True, если успешно
        """
        # TODO реализовать создание таблицы с темами для тестов
        return False

    def _create_questions_table(self) -> bool:
        """Метод по созданию таблицы с вопросами

        Returns:
            bool: True, если успешно
        """
        # TODO реализовать создание таблицы с вопросами, связав по ключу с таблицой тем
        return False

    def _create_answers_table(self) -> bool:
        """Метод по созданию таблицы с вариантами ответов на вопросы

        Returns:
            bool: True, если успешно
        """
        # TODO реализовать создание таблицы с вариантами ответов, связав по ключу с таблицой вопросов
        return False