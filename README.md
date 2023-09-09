# Задание

Реализовать функционал самообучения для студентов. <br><br>
Для этого необходимо создать платформу, 
которая работает только с авторизованными пользователями. <br>
Права доступа: только **авторизированные пользователи**<br><br>
На платформе необходимо предусмотреть функционал разделов и материалов.<br>
Модели:
- Разделы (Item)
- Материал (Materials)
- Вопросы (Questions)
- Ответы (Answers)
- Пользователь (UserCustom)<br><br>

Для каждого материала можно добавить тесты. <br><br>
Управление всеми сущностями необходимо реализовать через стандартный Django admin.<br><br>
Проверка ответа на тест осуществляется с помощью отдельного запроса на бэкенд. <br><br>
Реализовать либо Rest API, либо SSR с использованием Bootstrap. <br><br>
Для реализации проекта использовать фреймворк Django.<br><br>

---

## Описание программы

Программа - приложение для проверки знаний по нескольким разделам.
Пользователь может выбрать интересующий его раздел, 
в каждом разделе представлен ряд материалов (тем), по которым есть тесты.

Пользователь выбирает ответ, который на его взгляд верный. Приложение производить проверку ответа
и выводит результат пользователю.

По каждому материалу (теме) описано общее количество вопросов и процент выполнения.
Процент выполнения рассчитывается на основании правильных ответов пользователя по теме.

В приложении представлено 3 раздела и несколько подразделов (материалов):
- Математика
  - деление
  - умножение
  - сложение
- История
  - эпоха первых правителей Руси
  - великие географические открытия
- Английский
  - глагол to be
  - present Simple

В каждом подразделе есть ряд вопросов, на которые пользователь может ответить.

После завершения теста, если все вопросы верные, то изменяется статус теста на "завершен".

---

### Порядок работы с приложением через postman.

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
4. Добавление нового раздела (только модератор или админ)
```
GET запрос http://127.0.0.1:8000/item/create/
Body (JSON):
{
   "name": "Физика",
   "about": "В этом разделе будут представлены вопросы по физике."
}

Body response:
[

    ...
]
```
5. Добавление нового материала (только модератор или админ)
```
GET запрос http://127.0.0.1:8000/materials/create/
Body (JSON):
{
   "name_m": "квантовая физика"
}

Body response:
[

    ...
]
```
---

### Порядок работы с Django admin (только модератор или админ).

1. Панель Django admin
![Django admin](/staticfiles/image_readme/admin.png)
2. Список разделов
![Django admin_item](/staticfiles/image_readme/admin_item.png)<br>
Для добавления нового раздела необходимо нажать "добавить раздел+" сверху справа страницы.
Для удаления сразу нескольких разделов или одного необходимо выбрать нужные разделы (поставить галочки слева),
выбрать в "действие" удалить выбранные разделы и нажать выполнить.
Для просмотра какого-либо из разделов нужно нажать на pk раздела.
3. Добавление нового раздела
![Django admin_item](/staticfiles/image_readme/admin_add_item.png)<br>
В открывшемся окне необходимо заполнить информацию.
Для добавления Материалов нужно нажать на "+", если в списке нет нужного и добавить вручную.
В другом случае, если в списке указан нужный раздел, то нужно нажать на него (после этого он будет выделен),
если нужно несколько материалов (или другой показатель) через зажатый ctrl/cmd выбрать нужные.
Нажать Сохранить.
4. Список материалов
![Django admin_item](/staticfiles/image_readme/admin_materials.png)<br>
5. Изменение материала
![Django admin_item](/staticfiles/image_readme/admin_materials_change.png)<br>
6. Список ответов
![Django admin_item](/staticfiles/image_readme/admin_answers.png)<br>

По неописанным разделам/вопросам и тд логика работы аналогичная.

---

## Models:
1. Item:
    - name
    - about
    - materials (FK Materials)
    - user (MtoM UserCustom)
2. Materials:
    - name
    - question (FK Questions)
    - is_finished
    - count_questions
    - percent_complete
3. Questions:
   - title
   - is_active
   - is_finished
4. Answers:
   - question (FK Questions)
   - answer
   - user_answer
   - is_correct_answer
   - is_user_correct
5. UserCustom:
    - email
    - first_name
    - last_name
    - avatar
    - role

---

## Эндпоинты

1. User:
   - Регистрация
   - Авторизация
   - Выход из системы
2. Item:
   - Просмотр списка разделов
   - Выбор разделов
   - Детализированный просмотр отдного раздела со списком материалов
3. Materials:
   - Просмотр списка материалов
   - Детализированный просмотр отдельного материала со списком опубликованных вопросов
   - Отображение завершения материала
   - Количество вопросов в материале
   - Процент выполнения блока
4. Questions:
   - Детализированный просмотр вопроса со списком ответов
   - Завершен тест или нет
5. Answers:
   - Список ответов выводится по соответствующему вопросу
   - Выбор пользователем ответа, который ему кажется верным
   - Сверка ответа пользователя с правильным ответом
   - Вывод: правильный ответ или нет

---

## URL

1. User:
   - вход в систему пользователя `user/login`
   - выход из системы `user/logout`
   - регистрация пользователя `user/create`
2. Item:
   - список разделов `item/`
   - детализированный просмотр одного раздела `item/detail/<int:pk>`
3. Materials:
   - список материалов `materials/`???
   - детализированный просмотр одного материала `materials/detail/<int:pk>`???
4. Questions:
   - список вопросов `questions/`

---

## Body

### POST
#### user/login/: <br>
{<br>
   email: 'test@test.ru'<br>
   password: '123098'<br>
}<br>

#### user/create/: <br>
{<br>
   email: 'test2@test.ru'<br>
   password: '65490'<br>
}<br>