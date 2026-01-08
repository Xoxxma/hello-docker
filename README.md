# Hello Docker (Flask + Redis)

Небольшой Docker Compose проект с Flask и Redis.
Redis используется для хранения счётчика посещений страницы.

Запуск:
docker compose up -d --build

Открыть в браузере:
http://localhost:5000

Остановка:
docker compose down

Итог:
- Flask-приложение запущено в Docker
- Redis используется как хранилище
- Проект разворачивается одной командой
EOF
