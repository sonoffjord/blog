<h1 align="center">Simple Blog</h1>
<p align="center">Это простенький блог с возможностями: регистрации, авторизации, добавлением поста. </p>
<h3 align="center"> Стек </h3>

<div align="center"> 
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

</div>

<h3 align="center"> Как развернуть проект </h3>

1) Склонируйте  проект командой: <br>
   `git clone https://github.com/sonoffjord/blog.git`
2) Создайте виртуальное окружение: <br>
   `python -m venv venv`
3) Установите зависимости: <br>
   `pip install -r requirements.txt`
4) Установите новый `SECRET_KEY` в файле `config/settings.py`, взять новый можно например - [тут](https://djecrety.ir/).
5) Создайте миграцию и соберите статику: <br>
   `python manage.py makemigrations` <br>
   `python manage.py migrate` <br>
   `python manage.py collectstatic` <br>
6) Создайте суперпользователя: <br>
   `python manage.py createsuperuser`<br>

Готово! Запустите проект командой - `python manage.py runserver` и перейдите по адресу `127.0.0.1:8000` или `localhost`. <br>
Для перехода в админку перейдите - `127.0.0.1:8000/admin` и используйте логин и пароль при создании суперпользователя.

<hr>

Шаблон был взят [здесь](https://wowthemes.net/)
