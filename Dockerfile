# Используем базовый образ Python
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения в образ
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir aiogram openai

# Определяем команду для запуска бота
CMD ["python", "bot.py"]