# Копирование проекта на локальный компьютер

1. Создать новый проект в PyCharm.

2. Склонировать проект в PyCharm: <br>
`git clone https://github.com/Olga-Yar/FinalWork.git`
3. Нажать Enter
4. Перейти в папку приложения<br>
`cd FinalWork`
5. Установть виртуальное окружение:<br>
`python3 -m venv venv`
6. Активировать виртуальное окружение:<br>
`source venv/bin/activate` # macOS, Linux<br>
`venv\Scripts\activate` # Windows
7. В терминале в начале строки должно появиться "(venv)"
8. Должна появиться папка venv<br><br>

9. Установить все зависимости<br>
`pip3 install -r requirements.txt`
10. В файле .env и указать необходимые параметры:
- POSTGRES_NAME= # название вашей БД
- POSTGRES_USER= # имя пользователя
- POSTGRES_PASSWORD= # пароль для доступа к БД
11. Создать базу данных в postgres с именем, которое указали в файле .env
12. Создать миграции <br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`
13. Загрузить данные из файлов json в вашу БД<br>
`python3 manage.py loaddata study_data.json`<br>
`python3 manage.py loaddata user_data.json`
14. Запустить сервер<br>
`python3 manage.py runserver`

При успешном запуске в терминале появится:
```
System check identified no issues (0 silenced).
September 10, 2023 - 11:23:27
Django version 4.2.4, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
15. Остановка сервера:
`Ctrl+C`


**При работе на Windows вместо python3 и pip3 необходимо использовать python и pip.**
