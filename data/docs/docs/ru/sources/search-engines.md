> Источник: https://yandex.ru/support/metrica/ru/sources/search-engines
# Отчет «Поисковые системы»

- [Какие задачи может решать отчет](ru/sources/search-engines#case)
- [Структура и настройки отчета](ru/sources/search-engines#data)
- [Узнайте больше](ru/sources/search-engines#uznajte-bolshe)

Отчет содержит информацию о поисковых системах, которые привели посетителей на ваш сайт.

Посмотреть отчет: **Отчеты** → **Источники** → **Поисковые системы**.

Пример отчета можно увидеть на [демосчетчике Яндекс Метрики](https://metrika.yandex.ru/r/stat/search_engines?selected_rows=%5B%7B%22path%22%3A%5B%22google%22%5D%2C%22name%22%3A%5B%22Google%22%5D%7D%2C%7B%22path%22%3A%5B%22yandex%22%5D%2C%22name%22%3A%5B%22%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%22%5D%7D%2C%7B%22path%22%3A%5B%22duckduckgo%22%5D%2C%22name%22%3A%5B%22DuckDuckGo%22%5D%7D%2C%7B%22path%22%3A%5B%22yahoo%22%5D%2C%22name%22%3A%5B%22Yahoo!%22%5D%7D%2C%7B%22path%22%3A%5B%22bing%22%5D%2C%22name%22%3A%5B%22Bing%22%5D%7D%5D&period=month&confidence=%7B%22enabled%22%3Afalse%2C%22confidenceLevel%22%3A0.95%2C%22maxDeviation%22%3A0.05%7D).

Для определения данного источника Яндекс Метрика использует [реферер](https://ru.wikipedia.org/wiki/HTTP_referer). [Поисковые системы](ru/sources/search-engines#data), которые распознает Метрика.

Если вы хотите уточнить источник, используйте [UTM-метки](ru/general/source-tags#utm-construct) со следующими параметрами:

- `utm_medium` со значением `organic`.
- `utm_source`. В качестве значения задайте название поисковой системы: `yandex` — для поиска Яндекса; `google` — для поиска Google; `go.mail.ru` — для поиска Mail.ru.

Если в UTM-метке указано значение параметра `utm_source`, которое отсутствует в списке выше, Метрика отнесет визиты к источнику **Другая поисковая система: определено по меткам**.

## ru/sources/search-engines#caseКакие задачи может решать отчет

Вы можете узнать, из какой поисковой системы приходит больше посетителей и из какой меньше. Это поможет скорректировать работу по продвижению сайта в поиске.

Для этого достаточно развернуть древовидную структуру.

Сделать это можно, ориентируясь на показатель отказов. Чем выше показатель отказов, тем меньше сайт вовлекает посетителей — они уходят в течение 15 секунд, просмотрев только одну страницу.

Для этого нужно выделить [сегмент](ru/general/segmentation) с адресом определенной страницы сайта:

1. В группе условий **Визиты, в которых** нажмите значок .
2. Выберите условие **Поведение** → **Страница входа**.
3. В поле укажите адрес страницы.

Чтобы исключить данные с упоминанием бренда из отчета, воспользуйтесь сегментацией и добавьте условие вида `!@ваш_бренд` для русского и английского вариантов бренда, где:

- ! в начале — отрицание условия;
- @ в начале — вхождение строки (регистр не учитывается).

Например, для компании «Алиса в стране чудес» регулярное выражение может выглядеть `!@алиса в стране чудес` для русского варианта бренда и `!@alice in wonderland` — для английского. Этим способом можно убрать из отчета не более 20 фраз. Чтобы исключить более 20 фраз, используйте регулярное выражение `!~(бренд|бренд.рф|brend.ru)`.

## ru/sources/search-engines#dataСтруктура и настройки отчета

Данные в отчете объединены в группы:

- Поисковая система — обобщенное название сервиса, на котором есть поиск. Например, Яндекс. Список поисковых системМетрика распознает следующие системы: 7search.com Alexa Web Search Alhea All.by AltaVista arama.com Ask.com Babylon Search Baidu Biglobe Bigmir.net Bing blekko Coc Coc Conduit Crawler Cuil DAEMON search Daum Dogpile DuckDuckGo Ecosia Exalead.fr Finnerask.com Gigablast GMX Search Engine GoGo goo Google hakia hi.ru HotBot InfoSpace Istella KAZ.KZ Kvasir Live Search Lycos Magna Mail.Ru META Metabot.ru MetaCrawler MSN MyStart My Web Search Najdi.si NAVER NetSearch Nigma Onet Pivim Plusnetwork Poisk.ru Quintura Qwant Rambler Rx24 SAPO Scrub The Web Search Engine 1&1 Search Engine search.avg.com Search.com Search HandyCafe search.iminent.com search.incredibar.com search.smilebox.com search.softonic.com search.sweetim.com searchcompletion.com search-results.com searchya.com Seznam Seznam.cz so.360.cn sogou.com start.funmoods.com Startpagina Tut.by Ukr.net v9.com virgilio.it Web.de Webalta Wikia Search wp.pl Yaani Yahoo! yam.com Yippy Zapmeta Апорт (Aport) ГДЕ.РУ Гювеч (GBG.BG) Казах.ру Спутник Яндекс
- Поисковая фраза — запрос, по которому посетитель нашел в результатах поиска ссылку на ваш сайт и перешел по ней. Поисковые фразы могут не отображаться в отчете, если посещаемость за выбранный период меньше 10 посетителей и в отчет добавлена группировка или сегмент, потенциально деанонимизирующий посетителей. Например, “Страница входа”, “Возраст” и пр. Также в отчете может отображаться меньше информации, если поисковая система не передает данные в [реферере](https://ru.wikipedia.org/wiki/HTTP_referer).

Отчет поддерживает [все настройки](ru/reports/report-general), доступные в Яндекс Метрике.

Метрика определяет фразы, которые привели посетителей из Поиска Яндекса, по рефереру и [cookie](https://ru.wikipedia.org/wiki/Cookie) браузера. Cookie выставляется на домен, на который посетитель переходит из результатов поиска. Срок действия cookie ограничен. Метрика может не определить фразу по следующим причинам:

- Срок действия cookie закончился. Например, посетитель перешел по ссылке из результатов поиска и оставил страницу открытой на долгое время, затем обновил ее или закрыл.
- Страница, по ссылке на которую перешел посетитель из результатов поиска, перенаправила его на другой домен.
- Браузер посетителя блокирует cookie.

## ru/sources/search-engines#uznajte-bolsheУзнайте больше

- [Как Метрика определяет источник трафика](ru/general/sources-tracking)
- [Модели атрибуции](ru/reports/attribution-model)
- [Как узнать откуда идут внутренние переходы на сайт](ru/general/sources-qanda#internal)
- [Что такое Внутренние переходы](https://yandex.ru/blog/metrika-club/11985)
- [Почему выросло количество Внутренних переходов](https://yandex.ru/blog/metrika-club/vnutrennie-perekhody)
- [Как не терять источник трафика при переходе с домена на поддомен](https://yandex.ru/blog/metrika-club/kak-ne-teryat-istochnik-trafika-pri-perekhode-s-osnovnogo-domena-na-poddomen)

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
