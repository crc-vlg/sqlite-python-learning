from pydantic import BaseModel


class Student(BaseModel):
    """Модель учащегося
    """
    id: int
    last_name: str
    first_name: str
    age: int
    grade: str


class Theme(BaseModel):
    """Модель темы
    """
    # TODO Добавить поля для темы по образу Student


class Question(BaseModel):
    """Модель вопроса
    """
    # TODO Добавить поля для вопросов по образу Student


class Answer(BaseModel):
    """Модель ответа
    """
    # TODO Добавить поля для ответов по образу Student
