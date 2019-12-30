# fogstream-test-task
Тестовое задание для Fogstream


[![Build Status](https://travis-ci.com/gladunvv/fogstream-test-task.svg?token=dQu24woqyzrn82enuejL&branch=master)](https://travis-ci.com/gladunvv/fogstream-test-task)
[![codecov](https://codecov.io/gh/gladunvv/fogstream-test-task/branch/master/graph/badge.svg?token=eDRN1B3KKl)](https://codecov.io/gh/gladunvv/fogstream-test-task)



## Тестовое задание для Fogstream состоящее из двух частей

### Содержание:
* [Часть перавая](#часть-первая)
  + [Задание](#задание)
  + [Полезные ссылки](#полезные-ссылки)
  + [Requirements](#requirements)
  + [Сборка и запуск проекта](#сборка-и-запуск)
  + [Особенности](#особенности)
* [Часть вторая](#часть-вторая)
  + [Задание](#задание)

+ [License](#license)

## Часть первая:

### Задание:

Задание первой части заключалось в написании сайта, в котором пользователь может зарегистрироваться и авторизоваться, после чего ему становиться доступна форма отправки сообщения администратору. У сообщения после отправки(успешной или нет) в административной панели должна создаться запись с соответсвующим статусом. Также в шапке административной панели следует выводить общее количество отправленных писем и в скобках сколько из них не доставлено.

### Полезные ссылки:

+ [Django documentation](https://docs.djangoproject.com/en/2.2/)
+ [Django environ](https://django-environ.readthedocs.io/en/latest/)


### Requirements:
+ Django==3.0.1
+ coverage==5.0.1
+ django-environ==0.4.5
+ psycopg2==2.8.4
+ pytz==2019.3
+ sqlparse==0.3.0

### Сборка и запуск:
* Перед запуском необходимо локально создать и настроить базу данных(Postgresql), а также в корне проекта создать файл .env и заполнить его **данными для доступа к базе**, а также **данными для отправки почты** пример заполнения в [.env.example](https://github.com/gladunvv/library-api/blob/master/app/.env.example)

```bash
git clone git@github.com:gladunvv/fogstream-test-task.git
cd fogstream-test-task
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd app/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Особенности:
Каждое сообщение имеет три статуса отправки **Pending**, **Done**, **Sending error**, для отображения общего кол-ва сообщений и тех чья отправка закончилась ошибкой, в шапку административной панели был добавлен собственный templatetag.   
    
![](https://res.cloudinary.com/dtgupwmg6/image/upload/v1577599515/Screenshot_from_2019-12-29_14-53-48_fbtsjs.png)

## Часть вторая:

### Задание:
Заданием второй части было оптимизация базы данных, следовало нарисовать таблицы и связи которые получается после обработки предоставленной картинки.
    
![](https://github.com/gladunvv/fogstream-test-task/blob/master/best_data_base.jpeg)


### License
This project is licensed under the terms of the MIT license

