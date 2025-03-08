
# Инструкция по развертыванию Django-приложения

Это руководство поможет вам развернуть Django-приложение с использованием Docker и Python.

## Предварительные требования

Убедитесь, что у вас установлены:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (версия 3.8 или выше)

## Клонирование репозитория

Клонируйте репозиторий Django-приложением:

git clone https://github.com/AsaevichNikita/HoshivisionBack.git

cd HoshivisionBack

## Установка зависимостей
Установите зависимости, указанные в файле requirements.txt:

pip install -r requirements.txt

# Запуск приложения с помощью Docker

## Соберите Docker-образ:

docker-compose build
Запустите контейнеры:

docker-compose up
Если вы хотите запустить контейнеры в фоновом режиме, используйте:

docker-compose up -d
Приложение будет доступно по адресу: http://localhost:8000.

## Остановка контейнеров
Чтобы остановить контейнеры, выполните:

docker-compose down

## Миграции базы данных
Для выполнения миграций используйте

docker-compose exec web python manage.py makemigrations

docker-compose exec web python manage.py migrate

или если вы все разворачиваете без докера, то

python manage.py makemigrations
python manage.py migrate

## Создание суперпользователя
Чтобы создать суперпользователя, выполните:

docker-compose exec web python manage.py createsuperuser

## Логи
Чтобы просмотреть логи контейнера, выполните:

## docker-compose logs -f
Теперь ваше Django-приложение должно быть успешно развернуто! 🚀
