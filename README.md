# Построение RESTfull API для Yatube
### Стек технологий: Django, Django Rest Framework (DRF)

## Для чего этот проект?
Этот проект для изучения запросов и изучения API.
В данном проекте рассматриваются все виды: GET, POST, PATCH, PUT, DELETE операций, а также доступ по токену и ограничение прав.

## Особенности реализации

Настроена Аутентификация по JWT-токену. Ограничивает доступ на операции.
Все view-classes наследуются от ModelViewSet, что очень упрощает работу.
Для каждого view-класса используются свои сериализаторы, а возвращается Response(serializer.data) + status.
В проекте есть фильтрация (SearchFilter) для всех полей модели Post (DjangoFilterBackend) и не только.

## Что умеет данный проект?
Этот проект часть проекта Yatube - интернет-блога. В этой части появилась возможность обращаться к апи и делать различные запросы к нему
* Обработка всех видов запросов для постов (получить, изменить, удалить, создать (CRUD)), на операции предусмотренно ограничение по доступу
* Обработка запросов для комментариев
* Обработка запросов для отслеживаемых авторов конкретного пользователя
* Обработка запросов для групп

## Установка 
1. Клонируем проект
2. Устанавливаем пакеты pip install -r requirements.txt 
3. Запускаем в терминале командой /python manage.py runserver
4. API находится по адресу http://127.0.0.1:8000/api/v1/

### У проекта есть документация, при запуске проекта (runserver), можно перейти на /redoc, чтобы ознакомиться.