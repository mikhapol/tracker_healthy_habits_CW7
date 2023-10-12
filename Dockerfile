# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
# COPY requirements.txt .
COPY pyproject.toml .

# Устанавливаем зависимости
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Копируем код приложения в контейнер
COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]