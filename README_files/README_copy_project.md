# Копирование проекта на локальный компьютер

1. Создать новый проект в PyCharm.
2. С помощью терминала активировать виртуальное окружение, 
если PY не сделал это автоматически.
``
3. Инициировать git в проекте<br>
`git init`
4. Склонировать проект себе на компьютер: <br>
`git clone https://github.com/Olga-Yar/FinalWork.git`
5. Нажать Enter<br><br>

6. Установить все зависимости<br>
`pip3 install -r requirements.txt`
7. Создать файл .env и указать необходимые параметры, указанные в файле .env.sample
8. Создать базу данных в postgres с именем, которое указали в файле .env.sample
9. Создать миграции <br>
`python3 manage.py makemigrations`<br>
`python3 manage.py migrate`
10. Загрузить данные из файлов json в вашу БД<br>
`python3 manage.py load `
