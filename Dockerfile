# базовый образ с Python
FROM python:3.11-slim

# чтобы логи сразу выводились в консоль
ENV PYTHONUNBUFFERED=1

# рабочая папка внутри контейнера
WORKDIR /app

# копируем зависимости
COPY requirements.txt .

# устанавливаем библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# копируем приложение
COPY app.py .

# открываем порт для Flask
EXPOSE 5000

# команда запуска контейнера
CMD ["python", "app.py"]
