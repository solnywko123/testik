Простая система управления запасами продуктов с использованием RESTful API.

## Обзор проекта

Это приложение разработано в рамках стажировки Reviro TechStart - весна 2024. Он предоставляет возможность управления информацией о продуктах и учреждениях через RESTful API.

## Инструкции по созданию и запуску приложения с помощью Docker Compose

1. Клонируйте репозиторий:

```bash
git clone <ссылка на ваш репозиторий>
cd inventory

docker-compose up --build

docker-compose exec web python manage.py migrate

Краткое руководство по использованию API
Заведения (Establishments)
GET /establishments/: Получить список всех заведений.
GET /establishments/{id}/: Получить информацию о конкретном заведении.
POST /establishments/: Создать новое заведение.
PUT /establishments/{id}/: Обновить информацию о заведении.
DELETE /establishments/{id}/: Удалить заведение.
Продукты (Products)
GET /products/: Получить список всех продуктов.
GET /products/{id}/: Получить информацию о конкретном продукте.
POST /products/: Создать новый продукт.
PUT /products/{id}/: Обновить информацию о продукте.
DELETE /products/{id}/: Удалить продукт.
Для примеров запросов и ответов обратитесь к документации Swagger по адресу http://0.0.0.0:8000/docs/

Выполните следующую команду для запуска тестов в Docker:
docker-compose exec web pytest

Приложение использует PostgreSQL в качестве базы данных. Настройки прописаны в файле settings.py.


Результаты
Исходный код: git.com/solnywko123/testik
Dockerfile и docker-compose.yml: включены в репозиторий
Документация Swagger: http://localhost:8000/docs/
README: включен в репозиторий
Набор модульных тестов: включен в репозиторий






