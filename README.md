# REST API - User Management Service

REST API сервис для управления пользователями, реализующий базовые CRUD операции (создание, чтение, обновление, удаление). Можно гибко переключаться между различными типами хранилищ (база данных PostgreSQL или оперативная память)

##  Особенности

* **Чистая архитектура:** Разделение логики маршрутизации (API), бизнес-логики (сервисы) и работы с данными (репозитории).
* **Гибкое хранилище:** Поддержка работы как с In-Memory хранилищем, так и с реляционной БД PostgreSQL.
* **Асинхронность:** Полностью асинхронный стек вызовов (FastAPI + Asyncpg + SQLAlchemy 2.0).
* **Миграции:** Управление структурой базы данных с помощью Alembic.

##  Технологический стек

* **Язык:** Python 3.10+
* **Фреймворк:** FastAPI
* **База данных:** PostgreSQL
* **ORM:** SQLAlchemy (Async)
* **Миграции:** Alembic
* **Валидация:** Pydantic
* **Пакетный менеджер:** Poetry

##  Установка и запуск локально

### 1. Клонирование репозитория
```bash
git clone [https://github.com/StroylovV/test-task.git](https://github.com/StroylovV/test-task.git)
cd test-task
```
### 2. Проект использует Poetry для управления зависимостями.
```bash
poetry install
```
### 3. Настройка переменных окружения
Создайте файл .env и добавьте в него следующие настройки:
# Настройки подключения к базе данных PostgreSQL
```bash
DATABASE__POSTGRES_HOST=localhost
DATABASE__POSTGRES_PORT=5432
DATABASE__POSTGRES_USER=postgres
DATABASE__POSTGRES_PASSWORD=password
DATABASE__POSTGRES_DB=test-task
```
# Режим хранилища данных. Доступные значения: 'db' (PostgreSQL) или 'memory' (Оперативная память)
REPOSITORY_TYPE=db
4. Запуск сервера
poetry run python main.py

### Документация API
Основные эндпоинты:

    POST /users/ — Создание нового пользователя.

    GET /users/{id} — Получение данных пользователя по ID.

    PUT /users/{id} — Обновление ФИО пользователя.

    DELETE /users/{id} — Удаление пользователя.
  
