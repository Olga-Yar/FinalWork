# Копирование проекта на локальный компьютер

1. Создать новый проект в PyCharm.
2. При создании убедиться, что PY создаст новое виртуальное окружение 
![New Project](/staticfiles/image_readme/NewProject.png)<br>

После создания проекта, проверить что виртуальное окружение активировано:<br>
в терминале в начале строки должно стоять (venv)

3. Инициировать git в проекте<br>
`git init`
4. Склонировать проект в PyCharm: <br>
`git clone https://github.com/Olga-Yar/FinalWork.git`
5. Нажать Enter<br><br>

6. Установить все зависимости<br>
`pip3 install -r requirements.txt`
7. Создать файл .env и указать необходимые параметры:
- POSTGRES_NAME= # название вашей БД
- POSTGRES_USER= # имя пользователя
- POSTGRES_PASSWORD= # пароль для доступа к БД

8. Создать базу данных в postgres с именем, которое указали в файле .env
9. Создать миграции <br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`
10. Загрузить данные из файлов json в вашу БД<br>
`python3 manage.py loaddata study_data.json`
`python3 manage.py loaddata user_data.json`
11. Запустить сервер<br>
`python3 manage.py runserver`


При работе на Windows вместо python3 и pip3 необходимо использовать python и pip.
