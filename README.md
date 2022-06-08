### HARABOT (leng: RUS)

#### Проект: Промышленно-экономическая сфера "ОКВЭД"

##### Функционал программы:

+ извлечение кодов(классификаторов) и наименований видов деятельности "ОКВЭД".
+ извлечение общего колличества действующих организаций в каждом из видов деятельности описанных в классификаторе "
  ОКВЭД".
+ фильтрация от нежелательных элементов для сканирования.

##### Цель:

+ Собрать данные содержащие колличество организаций в определенных сферах деятельности.

#### ПРЕДВАРИТЕЛЬНЫЕ ШАГИ:

0. Должна быть установлена любая IDE и Python. (смотреть - Google).
1. В терминале установить Selenium.

- pip install selenium

2. Произвести первичную настройку Selenium
   (см. https://www.selenium.dev/documentation/webdriver/getting_started/).

##### Алгоритм:

+ Найти и открыть сайт содержащий исчерпывающую информацию о зарегестрированных организациях в стране.

+ Составить карту этого сайта (**список классификаторов ОКВЭД**).

+ Постранично просканировать необходимые секторы используя полученную карту.

+ Отфильтровать недействующие элементы - **мертвые души**.

+ Получить реальное колличество организаций в определенных сферах деятельности.

+ Сохранить в файл для сортировки и анализа (**В функционал данной программы закладывается только текстовая
  реализация**)
  Хотя можно сгрузить всё и в БД.

ОЖИДАЕМЫЙ РЕЗУЛЬТАТ:

- Файл result.txt сохранит в себе искомые данные.

##### Инструменты для реализации проекта:

> Для работы с браузером: [Selenium](https://selenium.dev/documentation/en/)

> Ресурсы для анализа:
[Rusprofile.ru](https://www.rusprofile.ru/codes/) / [МалыйБизнес.ru](https://www.malyi-biznes.ru/servisy/klassifikator-okved/)

> Для корректного форматирования данных и работ с таблицами: [LibreOffice](https://www.libreoffice.org/)

---

### HARABOT (leng: ENG)

#### Project: Industrial and Economic Sphere 'OKVED'

##### Functionality of the program:

+ extraction of codes (classifiers) and names of types of activities 'OKVED'.
+ extraction of the total number of operating organizations in each of the types of activities described in the OKVED
  classifier.
+ filtering from unwanted elements for scanning.

##### Goal:

+ Collect data containing the number of organizations in certain fields of activity.

##### Algorithm:

+ Find and open a site containing comprehensive information about registered organizations in the country.

+ Make a map of this site (**list of OKVED classifiers**).

+ Per-page to scan the necessary sectors using the received map.

+ Filter out inactive elements (**dead souls**).

+ Get a real number of organizations in certain areas of activity.

+ Save to file for sorting and analysis (**The functionality of this program is not laid**)

##### Tools for the implementation of the project:

> To work with the browser: [Selenium](https://selenium.dev/documentation/en/)

> Resources for analysis:
[Rusprofile.ru](https://www.rusprofile.ru/codes/) / [SmallBusiness.ru](https://www.malyi-biznes.ru/servisy/klassifikator-okved/)

> For the correct formatting of data and work with tables: [LibreOffice](https://www.libreoffice.org/)

## Discription of elements (leng: RUS)

**google chrome only**

> main.py

содержит необходимые настройки webdriver для управления Chrome.

> find_road.py

составляет маршрутный список для работы **page_scaner**.

так же получает список наименований требующихся далее для составления таблицы.

результат выполнения программы **page_scanner.py** требует форматирование полученных данных с помощью **filter.py**.

результат выполнения программы **filter.py** требует перемещения полученных данных в **map_road.py**.

#### Для работы find_road.py требуется:

> string_route_for_find_road.py

запустить ЭТОТ вспомогательный модуль и выполнить внутренние инструкции.

> page_scanner.py

сканирует каждую страницу ресурса.

считает количество валидных элементов.

сохраняет полученные данные в файл

> map_road.py

служит для указания маршрута действия **page_scanner.py**

заполняется вручную от **find_road.py**

- такой метод заполнения нужен для более гибкой настройки сканирования

> timing.py

реализует рандомные тайминги для обхода защиты сайта.
!!!!!!!!!!!!!!!!!!!!!!!!!!!ОДНАКО, вас всё равно выловят если будете использовать данный сборщик долго, ЗАБАНЯТ ПО IP.
Можно обойти защиту используя сторонние IP но зачем так заморачиваться. Это же тестовый проект.

> start.py

**после доработки планируется** использовать для большей автоматизации процесса выполнения программ в целом.

---

## Discription of elements (leng: ENG)

**google chrome only**

> main.py

Contains the necessary webdriver settings for managing Chrome.

> find_road.py

Compiles a route list for work **page_scaner**.

Also receives a list of items required later to compile the table.

Program execution result **page_scanner.py** requires formatting the received data with **filter.py**.

Program execution result **filter.py** requires moving the received data to **map_road.py**.

#### find_road.py requires:

> string_route_for_find_road.py

Run THIS auxiliary module and follow the internal instructions.

> page_scanner.py

Scans every page of the resource.

Counts the number of valid elements.

Saves the received data to a file.

> map_road.py

Serves to indicate the route of action **page_scanner.py**.

Manually populated by **find_road.py**.

- this filling method is needed for more flexible scan settings.

> timing.py

Implements random timings to bypass site protection.

> start.py

**after completion it is planned** to be used for greater automation of the program execution process as a whole.
