# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Для установки библиотек

```
pip install requirements.txt
```

## Для запуска программы

Запустите сайт командой:

```
python main.py
```

Также можете добавить аргументы `-p` и `-n`, путь до файла и название `.xlsx` файла соответственно.

Пример с файлом, находящимся в директории на уровень выше и имеющий название `wine3.xlsx`:

```
python main.py -p .. -n wine3.xlsx
```

## Пример оформления .xlsx файла

| Категория    | Название            | Сорт             | Цена  | Картинка                 | Акция                |
|--------------|---------------------|------------------|-------|--------------------------|----------------------|
| Белые вина   | Белая леди          | 	Дамский пальчик	| 399   | belaya_ledi.png	         | Выгодное предложение |
| Напитки      | Коньяк классический |                  | 350   | konyak_klassicheskyi.png |					            |
| Красные вина | Черный лекарь       | Качич            | 399	  | chernyi_lekar.png        |                      |



## Для проверки работы сайта

Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
