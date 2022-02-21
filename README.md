# Книга рецептов


### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

### Инициализация проекта

Команды выполняются внутри контейнера приложения:

```bash
docker-compose exec web bash
```

#### Применение миграций:

```bash
python manage.py migrate
```


#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

#### Добавление фикстур

```bash
python manage.py loaddata author ingredient recipe recipeingredient
```

Проект доступен по адресу http://127.0.0.1:8000
