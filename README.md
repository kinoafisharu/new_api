Даннное API имеет несколько разделов
 - kinoinfo/ - фильмы
 - texts/ - тексты
 - sounds/ - звук
 - products/ - всевозможные обучающие курсы - процессы
 
---! Для кадого листа и детального отображения применяются все стандартные REST запросы (Create, Read, Update, Delete) !---
(За редкими задокументированными исключениями)



Методы:
KINOINFO
1) kinoinfo/films/  ---  листинг фильмов,
    (POST и  GET)
2) kinoinfo/films/<int:pk> --- при добавлении идентификатора после слэша - подробно о фильме, применение детальных методов (REST)
    (принимает так же запросы PUT и DELETE) о REST запросах см. выше
3) kinoinfo/films/<int:pk>/like --- пост запрос к фильму, принимает параметр evaluation от 1 до 5, это тип лайка (1,2,3) или диз. (ост)

TEXTS
1) texts/stories   ---   листинг пользовательских историй, применение методов листинга (REST)
2) texts/stories/<int:pk> --- детальнно об истории, применение детальных методов (REST)
3) text/stories/orderby  --- GET запрос для сортировки историй по любому из полей (стандартные фильтры сортировки querusets  Django) параметры: ?by= (строка)  ?amount= (число)

Структура проекта ---
1) _main --- Сам проект, точка сборки, конфиги Django
2) _templates  --- HTML Темплейты (пока что один, для главной страницы с документацией)
3) API --- Место рендеринга главного темплейта с доками и ссылками на корни API, Место сборки всех корней API и дальнейшей их отправки в  _main
4) base --- Ключевая точка работы с базой данных и бекенд логики
5) management --- Консольные команды
6) products --- Сериализаторы и URLs интелектальных продуктов/процессов
7) soundprod --- Музыка/звуки и прочие вкусняшки в виде API
8) textprod ---  Текстовая информация API
9) kinoinfo --- Информация о фильмах!

    
Дев интерфейса: https://kinoafisha-vue-dev.herokuapp.com

Методы:
1) films - листинг фильмов с идами-гиперссылками


