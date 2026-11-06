-- создание таблицы с учениками
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    age INT NOT NULL,
    grade TEXT NOT NULL
);