## <img width="3%" title="Jenkins" src="images/logos/dex.png"> Проект UI автотестов домашней страницы https://dex-it.ru/

<!-- Технологии -->

### Используемые технологии/инструменты:
* Pytest
* Selene
* Allure
* Jenkins

<!-- Краткое описание -->

### Краткое описание:
Набор UI автотестов проверяет различные элементы домашней страницы компании DEX - открытие страницы, meta/SEO информацию, наличие h1 заголовка, номера телефона в хэдере, блока Клиенты, а также корректность ссылок в футере. Тесты написаны по Page Object шаблону, результаты собираются через Allure.

<!-- Тест кейсы -->

### Что проверяем:
* Открытие домашней страницы https://dex-it.ru/
* Проверка meta/SEO: title и непустой h1
* Проверка номера телефона компании в хэдере
* Хэдер страницы: проверка смены слов в анимации ("АНАЛИТИКА -> ДИЗАЙН -> РАЗРАБОТКА -> ПОДДЕРЖКА -> РАЗВИТИЕ"), которые циклично "печатаются" в этом блоке:

![This is an image](images/screenshots/typing_text_sequence.gif)

* Блок c логотипами клиентов: видимость логотипов, их количество
* Футер: проверка текста и ссылок в блоке "УСЛУГИ / КЕЙСЫ / ВАКАНСИИ"

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logos/jenkins.png"> Запуск проекта в Jenkins

##### При нажатии на "Build Now" начнется сборка тестов и их прохождение:
![This is an image](images/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logos/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете:
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов по их серьезности, времени прохождения, статусу и др.:
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся тест кейсы с описанными шагами, логами браузера и скриншотами:
![This is an image](images/screenshots/allure_suites1.png)
![This is an image](images/screenshots/allure_suites2.png)

<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logos/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах:
![This is an image](images/screenshots/tg_bot.png)

### Как запустить локально:
```bash
# создать виртуальное окружение
python -m venv venv
# активировать (Linux/macOS)
source venv/bin/activate
# (Windows)
# venv\Scripts\activate

# установить зависимости
pip install -r requirements.txt

# запустить тесты
pytest tests

# сформировать html–отчет, который откроется в браузере по умолчанию автоматически
allure serve tests/allure-results