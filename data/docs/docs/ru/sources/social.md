> Источник: https://yandex.ru/support/metrica/ru/sources/social
# Отчет «Социальные сети»

- [Какие задачи может решать отчет](ru/sources/social#case)
- [Структура и настройки отчета](ru/sources/social#data)

Отчет содержит данные о переходах из социальных сетей, позволяет отследить поведение таких посетителей и измерить показатели конверсии.

Посмотреть отчет: **Отчеты** → **Источники** → **Социальные сети**.

Пример отчета можно увидеть на [демосчетчике Яндекс Метрики](https://metrika.yandex.ru/r/stat/social-networks?period=month&selected_rows=%5B%7B%22path%22%3A%5B%22facebook%22%5D%2C%22name%22%3A%5B%22Facebook%22%5D%7D%2C%7B%22path%22%3A%5B%22twitter%22%5D%2C%22name%22%3A%5B%22Twitter%22%5D%7D%2C%7B%22path%22%3A%5B%22linkedin%22%5D%2C%22name%22%3A%5B%22Linked+in%22%5D%7D%2C%7B%22path%22%3A%5B%22reddit%22%5D%2C%22name%22%3A%5B%22Reddit%22%5D%7D%2C%7B%22path%22%3A%5B%22vkontakte%22%5D%2C%22name%22%3A%5B%22%D0%92%D0%9A%D0%BE%D0%BD%D1%82%D0%B0%D0%BA%D1%82%D0%B5%22%5D%7D%5D&confidence=%7B%22enabled%22%3Afalse%2C%22confidenceLevel%22%3A0.95%2C%22maxDeviation%22%3A0.05%7D).

Для определения данного источника Яндекс Метрика использует [реферер](https://ru.wikipedia.org/wiki/HTTP_referer) и [UTM-метки](ru/general/source-tags#utm-construct).

## ru/sources/social#caseКакие задачи может решать отчет

Отчет покажет, из каких социальных сетей приходят посетители на ваш сайт.

Сделать это можно, ориентируясь на показатель отказов. Чем выше показатель отказов, тем меньше сайт вовлекает посетителей — они уходят в течение 15 секунд, просмотрев только одну страницу.

## ru/sources/social#dataСтруктура и настройки отчета

Данные в отчете сгруппированы по социальным сетям, из которых пришли посетители сайта. Для некоторых соцсетей возможна детализация до уровня сообщества или группы на основе значений реферера.

Для более точного определения источника добавьте [UTM-метки](ru/general/source-tags#utm-construct) в URL и используйте полученную ссылку в социальных сетях. Ниже представлены значения, которые рекомендуем использовать в UTM-метках.

| Параметр | Обязательно | Значения |
| --- | --- | --- |
| utm_source | Да | vk , vkontakte , vk.com — для Вконтакте; facebook , fb , facebook.com — для Facebook * ; twitter или twitter.com — для Twitter; ok , odnoklassniki , ok.ru или odnoklassniki.ru — для Одноклассники; livejournal — для Живой Журнал; plus.google.com или googleplus — для Google+; my.mail.ru — для Мой мир Mail.ru; linkedin или linkedin.com — для LinkedIn; delicious — для delicious; tumblr или tumblr.com — для Tumblr; instagram или instagram.com — для Instagram * ; pinterest.com — для Pinterest; reddit — для Reddit; stumbleupon — для StumbleUpon. Если в UTM-метке указано значение параметра utm_source , которое отсутствует в списке выше, Метрика определяет источник перехода по значению параметра utm_medium . При этом в отчете такие визиты будут отнесены к источнику Другая социальная сеть: определено по меткам |
| utm_medium | Да | social social-network social-media sm social network social media |

* Сервис, запрещенный на территории РФ.

Если на сайте-источнике есть JavaScript-редирект или переход происходит с сайта с протоколом HTTPS на сайт с протоколом HTTP, используйте метку [utm_referrer](ru/general/source-tags#utm-referrer).

Отчет поддерживает [все настройки](ru/reports/report-general), доступные в Яндекс Метрике.

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

Сервис, запрещенный на территории РФ.

### Была ли статья полезна?
