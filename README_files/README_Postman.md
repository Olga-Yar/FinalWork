# Порядок работы с приложением через postman.
1. Авторизация - в приложении используется авторизация JWTAuthentication
```
POST запрос http://127.0.0.1:8000/user/token/
Body (JSON):
{
   "email": "test@test.ru",
   "password": "12###8"
}

Body response:
{
    "refresh": "ey###Ow",
    "access": "ey###Og"
}

Access token необходим для доступа в приложение.
Данный access token нужо вставить на другую (рабочую) вкладку postman:
Headers - прописать ключ Authorization - Value=Bearer и через пробел вставить access token.

Данный тип авторизации для безопастности доступа имеет ограниченный период действия токена - 5 минут.
По истечении указанного времени необходимо обновить токен путем повторной отправки get запроса.


При истеченном токене, при попытки сделать любой запрос, вывелется ошибка:
{
    "detail": "Данный токен недействителен для любого типа токена",
    "code": "token_not_valid",
    "messages": [
        {
            "token_class": "AccessToken",
            "token_type": "access",
            "message": "Токен недействителен или просрочен"
        }
    ]
}
```
2. Вывод списка разделов.
```
GET запрос http://127.0.0.1:8000/item/
Body (JSON):
None

Body response:
[
    {
        "name": "История",
        "about": "В данном разделе можно проверить себя на знание основных исторических фактов.",
        "materials_name": [
            "Великие географические открытия:",
            "Эпоха первых правителей Руси:"
        ]
    },
    {
        "name": "Английский язык",
        "about": "",
        "materials_name": [
            "Present Simple",
            "Глагол to be"
        ]
    },
    ...
]
```
3. Вывод списка материалов.
```
GET запрос http://127.0.0.1:8000/materials/
Body (JSON):
None

Body response:
[
    {
        "pk": 8,
        "name_m": "Деление",
        "question_title": [
            "3/2",
            "6/3",
            "44/2",
            "63/9",
            "121/11",
            "169/13"
        ],
        "is_finished": false,
        "count_questions": 6,
        "percent_complete": 0.0
    },
    {
        "pk": 7,
        "name_m": "Умножение",
        "question_title": [
            "5*5",
            "2*3",
            "7*0",
            "15*69"
        ],
        "is_finished": false,
        "count_questions": 4,
        "percent_complete": 0.0
    },
    ...
]
```
3. Вывод списка вопросов.
```
GET запрос http://127.0.0.1:8000/questions/
Body (JSON):
None

Body response:
[
    {
        "pk": 30,
        "title": "Какое государство полностью разбил Святослав ?",
        "answer_name": [
            "Хазарский каганат",
            "Печенеги",
            "Византийскию империю"
        ],
        "is_active": true,
        "is_finished": false
    },
    {
        "pk": 29,
        "title": "Годы правления Вещего Олега ?",
        "answer_name": [
            "862-879",
            "879-912",
            "912-945",
            "945-972"
        ],
        "is_active": true,
        "is_finished": false
    },
    ...
]
```
Добавление разделов, материалов, вопросов и тд необходимо делать через Django admin,
однако, данный функционал доступен и через postman.

4. Добавление нового раздела (только модератор или админ)
```
PUT запрос http://127.0.0.1:8000/item/create/
Body (JSON):
{
   "name": "Физика",
   "about": "В этом разделе будут представлены вопросы по физике."
}

Body response:
{
    "name": "Физика",
    "about": "В этом разделе будут представлены вопросы по физике.",
    "materials_name": []
}
```
5. Добавление нового материала (только модератор или админ)
```
PUT запрос http://127.0.0.1:8000/materials/create/
Body (JSON):
{
   "name_m": "квантовая физика",
   "percent_complete": "0.0"
}

Body response:
{
    "pk": 13,
    "name_m": "квантовая физика",
    "question_title": [],
    "is_finished": false,
    "count_questions": 0,
    "percent_complete": 0.0
}
```