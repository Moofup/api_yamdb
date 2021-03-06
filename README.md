# Проект api_yamdb

## Описание

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title).
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий (Category) и жанров (Genre) может быть расширен
Отзывы могут комментироваться пользователями (Comments) 

## Алгоритм регистрации пользователей
Пользователь отправляет POST-запрос с параметром email на `/api/v1/auth/email/`.
YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
Пользователь отправляет POST-запрос с параметрами email и confirmation_code на `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
Эти операции выполняются один раз, при регистрации пользователя. В результате пользователь получает токен и может работать с API, отправляя этот токен с каждым запросом.
## Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
**Аутентифицированный пользователь (user)** — может читать всё, как и Аноним, дополнительно может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.
**Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять и редактировать любые отзывы и комментарии.
**Администратор (admin)** — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
**Администратор Django** — те же права, что и у роли Администратор.
## Установка
Склонируйте репозиторий. Находясь в папке с кодом создайте виртуальное окружение `python -m venv venv`, активируйте его (Windows: `source venv\scripts\activate`; Linux/Mac: `sorce venv/bin/activate`), установите зависимости `python -m pip install -r requirements.txt`.
Для запуска сервера разработки,  находясь в директории проекта выполните команды:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

##  Примеры запросов к API:

Получение списка всех категорий:
```
http://127.0.0.1:8000/api/v1/categories/
```
Получение списка всех жанров:
```
http://127.0.0.1:8000/api/v1/genres/
```
Получение списка всех произведений:
```
http://127.0.0.1:8000/api/v1/titles/
```
Получение информации о произведении с ID=1
```
http://127.0.0.1:8000/api/v1/titles/1/
```
Получение списка всех отзывов для произведения с ID=1:
```
http://127.0.0.1:8000/api/v1/titles/1/reviews/
```
Получение информации об отзыве с ID=1 для произведения с ID=1:
```
http://127.0.0.1:8000/api/v1/titles/1/reviews/1/
```
Получение списка комментариев об отзыве с ID=1 для произведения с ID=1:
```
http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/
```
Получение комментария с ID=1 об отзыве с ID=1 для произведения с ID=1:
```
http://127.0.0.1:8000/api/v1/titles/1/reviews/1/comments/1/
```
Получение списка всех пользователей (Права доступа: Администратор):
```
http://127.0.0.1:8000/api/v1/users/
```
Получение информации о пользователе user1 (Права доступа: Администратор):
```
http://127.0.0.1:8000/api/v1/users/user1/
```
