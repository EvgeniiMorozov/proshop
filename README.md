## ProShop

### Разработка онлайн-магазина

---

## Проект в разработке !!!

---

#### Back-end:

- Django
- Django REST framework

#### Front-end:

- React v.18
- Redux
- React-router v.6
- React-Bootstrap

#### Database:

- SQlite3

### Запуск проекта

Скопируйте проект на компьютер

```
gh repo clone EvgeniiMorozov/proshop
cd proshop
```

Создайте и активируйте виртуальное окружение, установите зависимости для бэкэнда:

```
python -m venv .venv

./.venv/Scripts/activate.cmd

pip install -r requirements.txt
```

Сделайте миграции:

```
python ./backend/manage.py migrate
```

Установите зависимости бля фронтэнда:

```
./frontend/npm init
```

Запустите проект:

```
./backend/manage.py runserver
./frontend/npm start
```
