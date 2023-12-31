
# Порядок работы с Django admin 
(только модератор или админ).

Переход в админку: http://127.0.0.1:8000/admin

1. Панель Django admin
![Django admin](https://github.com/Olga-Yar/FinalWork/blob/main/staticfiles/image_readme/admin.png)
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