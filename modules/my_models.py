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
    id: int
    name: str


class Question(BaseModel):
    """Модель вопроса
    """
    id: int
    quiestion: str


class Answer(BaseModel):
    """Модель ответа
    """
    id: int
    answer: str
