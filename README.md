# ProShop

## Разработка онлайн-магазина

---

## Проект в разработке

---

### Back-end

- Django
- Django REST framework

### Front-end

- React v.18
- Redux
- React-router v.6
- React-Bootstrap

### Database

- SQlite3

### Запуск проекта

Скопируйте проект на компьютер

```bash
gh repo clone EvgeniiMorozov/proshop
cd proshop/services
```

Создайте и активируйте виртуальное окружение, установите зависимости для бэкэнда:

```bash
python -m venv .venv

./.venv/Scripts/activate.cmd

pip install -r requirements.txt
```

Сделайте миграции:

```bash
python ./backend/manage.py migrate
```

Установите зависимости бля фронтэнда:

```bash
./frontend/npm init
./frontend/npm build
```

Запустите проект:

```bash
./backend/manage.py runserver
```
