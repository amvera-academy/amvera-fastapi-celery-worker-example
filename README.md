# Общий Celery worker на Amvera

Простой пример деплоя Celery worker в [Amvera](https://amvera.ru).

Worker не зависит от FastAPI, Flask или Django. Он получает задачу `process_text` через Redis и возвращает переданную строку в верхнем регистре.

[ОБЩАЯ ИНСТРУКЦИЯ ПО CELERY](https://github.com/amvera-services/amvera-fastapi-example/blob/main/CELERY.md) | [КАК ЗАПУСТИТЬ НА AMVERA](#деплой-в-amvera)

## Локальный запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export REDIS_URL=redis://localhost:6379/0
celery --app worker worker --loglevel=INFO --concurrency=1
```

## Деплой в Amvera

Создайте Redis и отдельное приложение для worker в одном регионе, загрузите этот репозиторий и добавьте переменную `REDIS_URL`.

Полная схема подключения и пример отправки задачи описаны в общей [инструкции по Celery](https://github.com/amvera-services/amvera-fastapi-example/blob/main/CELERY.md).
