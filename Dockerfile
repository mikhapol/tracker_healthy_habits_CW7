# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY poetry.lock pyproject.toml /app/

# Устанавливаем зависимости
# RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install poetry

RUN poetry install --no-root

# Копируем код приложения в контейнер
COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]