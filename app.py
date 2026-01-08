from flask import Flask
import redis
import os

# создаём Flask-приложение
app = Flask(__name__)

# подключаемся к Redis
# host = имя сервиса из docker-compose.yml
redis_client = redis.StrictRedis(
    host='redis',
    port=6379,
    decode_responses=True
)

# главная страница
@app.route('/')
def hello():
    # увеличиваем счётчик просмотров в Redis
    count = redis_client.incr('hits')

    # возвращаем текст в браузер
    return f"Hello from Docker! This page has been viewed {count} times."

if __name__ == '__main__':
    # порт берём из переменной окружения
    port = int(os.environ.get('APP_PORT', 5000))

    # запускаем сервер и слушаем все интерфейсы
    app.run(host='0.0.0.0', port=port)
