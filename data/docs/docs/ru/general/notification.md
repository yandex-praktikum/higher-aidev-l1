> Источник: https://yandex.ru/support/metrica/ru/general/notification
# Предупреждение о сборе статистики

- [Пример оповещения](ru/general/notification#exmp)
- [Пример реализации кода](ru/general/notification#code)

Вы можете предупредить посетителей вашего сайта о сборе статистики и отложить [загрузку кода счетчика Яндекс Метрики](ru/general/how-it-works#data_extract_pull) на страницах сайта.

При согласии посетителя на передачу информации код счетчика [загружается стандартным образом](ru/general/how-it-works#data_extract_pull). Без согласия посетителя код не загрузится. Однократный выбор посетителя может учитываться при посещении всех страниц сайта (домена).

Чтобы включить оповещение и реализовать отложенную загрузку кода счетчика, обратитесь к вашему вебмастеру.

## ru/general/notification#exmpПример оповещения

Вы можете использовать любой текст для информирования посетителей. Представленный ниже текст приведен исключительно в качестве примера отображения текста в оповещении. Яндекс не несет ответственности за его соответствие требованиям законодательства. Перед размещением текста рекомендуем  проконсультироваться с вашим юристом.

Этот сайт собирает статистику посещения и данные посетителей.

[Ссылка на Пользовательское соглашение вашего сайта или на Политику конфиденциальности вашего сайта]

## ru/general/notification#codeПример реализации кода

```
...
<head>
    <meta charset="UTF-8">
    <title>Заголовок страницы</title>
    <!--В примере используется стиль reset.css. Вы можете использовать свое решение.-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
    <!--В примере используется библиотека js-cookie для работы с cookie. Вы можете использовать свое решение-->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.1.2/js.cookie.js"></script>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            width: 100%;
            height: 100%;
        }
        .cookie-notification {
            position: fixed;
            background-color: rgba(0, 0, 0, .8);
            bottom: 0;
            width: 100%;
            color: white;
            padding: 15px;
        }
        .cookie-notification_hidden_yes {
            display: none;
        }
        .cookie-notification__header {
            margin-bottom: 10px;
            font-size: 23px;
        }
        .cookie-notification__body {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    Контент сайта
    <div class="cookie-notification cookie-notification_hidden_yes">
        <div class="cookie-notification__header">Предупреждение о сборе статистики</div>
        <div class="cookie-notification__body">
       <p>Этот сайт собирает статистику посещения и данные посетителей.</p>
       <p>[Ссылка на Пользовательское соглашение вашего сайта или на Политику конфиденциальности вашего сайта]</p>
        </div>
        <div class="cookie-notification__buttons">
            <button class="cookie-notification__button" id="yes">Я согласен</button>
        </div>
    </div>
    <script type="text/javascript">
        // Загружаем сам код счетчика сразу
        (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
        (window, document,'script','https://mc.yandex.ru/metrika/tag.js', 'ym')

        var messageElement = document.querySelector('.cookie-notification');
        // Если нет cookies, то показываем плашку
        if (!Cookies.get('agreement')) {
            showMessage();
        } else {
            initCounter();
        }
        // Функция добавляет класс к DOM-элементу. Вы можете использовать библиотеку jQuery или другой фреймворк
        function addClass (o, c) {
            var re = new RegExp("(^|\\s)" + c + "(\\s|$)", "g");
            if (!o || re.test(o.className)) {
                return;
            }
            o.className = (o.className + " " + c).replace(/\s+/g, " ").replace(/(^ | $)/g, "");
        }
        // Функция удаляет класс из DOM-элемента. Вы можете использовать библиотеку jQuery или другой фреймворк
        function removeClass (o, c) {
            var re = new RegExp('(^|\\s)' + c + '(\\s|$)', 'g');
            if (!o) {
                return;
            }
            o.className = o.className.replace(re, '$1').replace(/\s+/g, ' ').replace(/(^ | $)/g, '');
        }
        // Функция, которая прячет предупреждение
        function hideMessage () {
            addClass(messageElement, 'cookie-notification_hidden_yes');
        }
        // Функция, которая показывает предупреждение
        function showMessage () {
            removeClass(messageElement, 'cookie-notification_hidden_yes');
        }
        function saveAnswer () {
            // Прячем предупреждение
            hideMessage();

            // Ставим cookies
            Cookies.set('agreement', '1');
        }
        function initCounter () {
            ym(XXXXXXXX, 'init', {});
            saveAnswer();
        }
        // Нажатие кнопки "Я согласен"
        document.querySelector('#yes').addEventListener('click', function () {
            initCounter();
        });
    </script>
</body>
...
```

```
...
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
    <!--This example uses the reset.css style. You can use your own approach.-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
    <!--The example uses the js-cookie library for working with cookies. You can use your own approach-->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/2.1.2/js.cookie.js"></script>
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            width: 100%;
            height: 100%;
        }
        .cookie-notification {
            position: fixed;
            background-color: rgba(0, 0, 0, .8);
            bottom: 0;
            width: 100%;
            color: white;
            padding: 15px;
        }
        .cookie-notification_hidden_yes {
            display: none;
        }
        .cookie-notification__header {
            margin-bottom: 10px;
            font-size: 23px;
        }
        .cookie-notification__body {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    Website Content
    <div class="cookie-notification cookie-notification_hidden_yes">
        <div class="cookie-notification__header">Statistics Collection Notice</div>
        <div class="cookie-notification__body">
       <p>This website collects visit statistics and visitor data.</p>
       <p>[Link to your website's User Agreement or Privacy Policy]</p>
        </div>
        <div class="cookie-notification__buttons">
            <button class="cookie-notification__button" id="yes">I Agree</button>
        </div>
    </div>
    <script type="text/javascript">
        // Load the code snippet immediately
        (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
        (window, document,'script','https://mc.yandex.ru/metrika/tag.js', 'ym')

        var messageElement = document.querySelector('.cookie-notification');
        // If there are no cookies, show the banner
        if (!Cookies.get('agreement')) {
            showMessage();
        } else {
            initCounter();
        }
        // Function adds a class to a DOM element. You can use the jQuery library or another framework
        function addClass (o, c) {
            var re = new RegExp("(^|\\s)" + c + "(\\s|$)", "g");
            if (!o || re.test(o.className)) {
                return;
            }
            o.className = (o.className + " " + c).replace(/\s+/g, " ").replace(/(^ | $)/g, "");
        }
        // Function removes a class from a DOM element. You can use the jQuery library or another framework
        function removeClass (o, c) {
            var re = new RegExp('(^|\\s)' + c + '(\\s|$)', 'g');
            if (!o) {
                return;
            }
            o.className = o.className.replace(re, '$1').replace(/\s+/g, ' ').replace(/(^ | $)/g, '');
        }
        // Function that hides the warning
        function hideMessage () {
            addClass(messageElement, 'cookie-notification_hidden_yes');
        }
        // Function that shows the warning
        function showMessage () {
            removeClass(messageElement, 'cookie-notification_hidden_yes');
        }
        function saveAnswer () {
            // Hide the warning
            hideMessage();

            // Set cookies
            Cookies.set('agreement', '1');
        }
        function initCounter () {
            ym(XXXXXXXX, 'init', {});
            saveAnswer();
        }
        // Click on the "I Agree" button
        document.querySelector('#yes').addEventListener('click', function () {
            initCounter();
        });
    </script>
</body>
...
```

где `XXXXXXXX` — номер вашего счетчика.

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
