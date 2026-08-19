> Источник: https://yandex.ru/support/metrica/ru/general/source-tags
# Как Метрика обрабатывает метки

- [Как правильно сформировать метку](ru/general/source-tags#form-rules)
- [Отображение меток в отчетах](ru/general/source-tags#report)[Узнайте больше](ru/general/source-tags#uznajte-bolshe)
- [Вопросы и ответы](ru/general/source-tags#qanda)

Яндекс Метрика учитывает любые переходы по ссылке с *меткой*. Например, прямой заход по ссылке, сохраненной в браузере или переход из почтовой рассылки. Метрика умеет обрабатывать следующие виды меток:

| Метка | Примечание |
| --- | --- |
| UTM | Для меток формируются стандартные отчeты . Данные по метке utm_referrer можно отслеживать в отчетах По параметрам URL и Сайты . Чтобы метка попала в отчет, она должна быть составлена корректно . Также по UTM-меткам формируются отчеты Рекламные системы , Социальные сети , Мессенджеры , Рекомендательные системы |
| Openstat |  |
| from |  |
| yclid | Метка проставляется Яндекс Директом. Пример: https://example.com/?yclid=123 Данные о переходах с объявлений доступны в группе отчетов «Директ»: Директ, сводка Директ, площадки Директ, расходы В них статистика подсчитывается только по учтенным кликам — не отфильтрованным системой защиты от скликивания |
| ymclid | Метка выставляется Яндекс Маркетом. Данные о переходах с Яндекс Маркета смотрите в отчете Рекламные системы . Пример: https://example.com/?ymclid=123 |
| ysclid | Метка используется для определения поисковых фраз из поиска Яндекса. Пример: https://example.com/?ysclid=a1bc2 Фразы можно увидеть в отчете Поисковые запросы |
| gclid | Используется для отслеживания рекламы Google Ads. Для определения источников с меткой gclid используйте сегментацию . Пример: https://example.com/?gclid=123 |
| yqrid | Используется для отслеживания переходов по QR-коду . Данные о переходах смотрите в отчете Источники, сводка . Пример: https://example.com/?yqrid=abc |
| yzclid | Метка выставляется Яндекс Промостраницами. Данные о переходах с Яндекс Промостраниц смотрите в отчете Рекламные системы . Пример: https://example.com/?yzclid=123 |

Яндекс Метрика получает информацию о метке из **первого** просмотра в течение визита посетителя. Если в первом просмотре метки нет, то она не учитывается для всего визита.

Параметры меток, по которым определяется источник:

| Рекламные системы | Почтовые рассылки | Соцсети, сайты | Поисковые системы, мессенджеры | Рекомендательные системы |
| --- | --- | --- | --- | --- |
| utm_source , utm_medium , openstat_service , gclid | from , utm_medium , openstat_service | utm_source , utm_medium , utm_referrer | utm_source , utm_medium | utm_source , utm_medium |

Примечание

Содержимое меток распознается корректно, если на сайте используется [кодировка UTF-8](https://ru.wikipedia.org/wiki/UTF-8).

## ru/general/source-tags#form-rulesКак правильно сформировать метку

Первый параметр всегда добавляется после символа «?», все последующие — после «&». Также в метках должны отсутствовать лишние символы (например, %2B).

| Параметр | Описание | Примечание |
| --- | --- | --- |
| utm_source | Источник трафика | Метка обязательна при отслеживании переходов из социальных сетей и рекламных систем, кроме Яндекс Директа |
| utm_medium | Канал трафика | Метка обязательна при отслеживании переходов по QR-кодам, из социальных сетей, мессенджеров, почтовых рассылок и рекомендательных систем. По значению utm_medium робот будет отправлять источник в раздел Другие рекомендательные системы , это является обязательным условием для нестандартных рекомендательных систем, которые не распознаются по рефереру |
| utm_campaign | Название кампании | — |
| utm_content | Содержание кампании | — |
| utm_term | Ключевая фраза | — |

- `adfox` — для Adfox;
- `admitad` — для Admitad;
- `adnews` — для AdNews;
- `adnous` — для ADNOUS;
- `adriver` — для AdRiver;
- `advcake` — для ADV.Cake;
- `advmaker` — для Advmaker.ru;
- `aport (aport.ru)` — для Апорт;
- `avito (avito_ads, avito-ads, avitoads)` — для Avito Ads
- `AvitoPromo` — для Avito Промо;
- `begun` — для Begun;
- `bing` — для Bing Ads;
- `B2BContext` — для B2BContext;
- `city_ads` — для CityAds Media;
- `criteo` — для Criteo;
- `directadvert (directadvert.ru)` — для Direct/ADVERT;
- `drivenetwork` — для DriveNetwork;
- `epn, epnbz` — для E.PN;
- `facebook (fb, facebook.com, fb.com)` — для Facebook***;
- `flocktory` — для Flocktory;
- `gdeslon, gdeslon_cpa` — для Где Слон?;
- `giraffio` — для giraffe.io (AppCity);
- `google (adwords, adsense)` — для Google;
- `instagram` — для Instagram***;
- `kavanga` — для Каванга;
- `ladycenter` — Ladycenter;
- `link` — для ЛинкРУ;
- `magna` — для Magna Context;
- `marketgid` — для МаркетГид;
- `medialand` — для Medialand;
- `merchant` — для Google Merchant;
- `moimir` — для Мой мир Mail.ru;
- `nnn (nnn.ru)` — для NNN (National News Network);
- `odnoklassniki` — для Одноклассники;
- `ozon` — для Ozon;
- `perfluence` — для Perfluence;
- `price (price.ru, priceru, price-gmc)` — для Price.ru;
- `prre` — для PRRE.RU;
- `rtbhouse` — для RTB House;
- `mytarget (targetmailru)` — для myTarget (Target Mail.ru);
- `taboola` — для Taboola;
- `telegram_ads, tg_ads, tgads` — для Telegram;
- `tiktok` — для TikTok;
- `torg.mail.ru` — для Товары Mail.ru;
- `trorer (rorer)` — для RORER;
- `Ttarget` — для tTarget;
- `videonow` — для Videonow.ru;
- `vkontakte (vk, vk.com)` — для ВКонтакте;
- `vk_ads, vkads, vk-ads, vkr` — для VK Реклама;
- `whisla` — для Whisla;
- `youtube` — для YouTube.

- `vk`, `vkontakte`, `vk.com` — для Вконтакте;
- `facebook`, `fb`, `facebook.com` — для Facebook***;
- `twitter` или `twitter.com` — для Twitter;
- `ok`, `odnoklassniki`, `ok.ru` или `odnoklassniki.ru` — для Одноклассники;
- `livejournal` — для Живой Журнал;
- `plus.google.com` или `googleplus` — для Google+;
- `my.mail.ru` — для Мой мир Mail.ru;
- `linkedin` или `linkedin.com` — для LinkedIn;
- `delicious` — для delicious;
- `tumblr` или `tumblr.com` — для Tumblr;
- `instagram` или `instagram.com` — для Instagram***;
- `pinterest.com` — для Pinterest;
- `reddit` — для Reddit;
- `stumbleupon` — для StumbleUpon.

- `skype` — для Skype;
- `telegram, tg` — для Telegram;
- `viber` — для Viber;
- `wechat` — для WeChat;
- `whatsapp` — для WhatsApp.

- `mirtesen` — для МирТесен;
- `rambler` — для Rambler.

- `yandex` — для поиска Яндекса;
- `google` — для поиска Google;
- `go.mail.ru` — для поиска Mail.ru.

Если в UTM-метке указано значение параметра `utm_source`, которое отсутствует в списке выше, Метрика отнесет визиты к источнику **Другая поисковая система: определено по меткам**.

- `banner`
- `cpa`
- `cpc`
- `cpm`
- `cpp`
- `cpv`
- `display`
- `paidsearch`
- `ppc`

- `social`
- `social-network`
- `social-media`
- `sm`
- `social network`
- `social media`

- `rec`

- `organic`

- `email` или `e-mail` — для переходов с почтовых рассылок;
- `qr` или `qrcode` — для переходов по QR-кодам;
- `messenger` — для переходов из [мессенджеров](ru/sources/messenger).

Примечание

Если в `utm_source` используется значение из списка рекомендуемых, а в `utm_medium` указано значение не из списка, то Метрика определяет источник перехода по `utm_source`. Это относится к источникам трафика, для которых метка `utm_medium` необязательна.

Если вы используете в метке не все параметры, обратите внимание на их последовательность:

```
https://example.com/?utm_source=link&utm_medium=cpc&utm_campaign=new
```

##### ru/general/source-tags#utm-referrerutm_referrer

Чтобы Яндекс Метрика правильно определила источник перехода на сайт при JavaScript-редиректе или при переходе на ваш сайт с протоколом HTTP с сайта, доступного по протоколу HTTPS, используйте параметр `utm_referrer`.

[Почему могут не фиксироваться переходы с определенных сайтов](ru/general/sources-qanda#site-https)

В качестве значения укажите адрес сайта, с которого совершен переход. Пример:

```
https://example.com/?utm_referrer=example-source.com
```

где

- `example.com` — это ваш сайт;
- `example-source.com` — это сайт, с которого происходит переход.

Если в качестве значения вы указываете полный адрес сайта, со схемой HTTP или HTTPS, то такой URL нужно кодировать. Например, вы хотите указать адрес `https://example.com`. Закодированный адрес будет выглядеть так: `https%3A%2F%2Fexample.com`.

В метке Openstat параметры перечисляются через символ «;».

```
https://example.com/?_openstat=openstat_service;openstat_campaign;openstat_ad;openstat_source
```

где

- `openstat_service` — источник трафика;
- `openstat_campaign` — идентификатор кампании;
- `openstat_ad` — идентификатор объявления;
- `openstat_source` — идентификатор площадки.

Пример:

```
https://example.com/?_openstat=adfox;moscow;discount;top
```

Используйте следующие значения для отслеживания переходов из рекламных систем:

- `adfox` — для Adfox;
- `admitad` — для Admitad;
- `adnews` — для AdNews;
- `adnous` — для ADNOUS;
- `adriver` — для AdRiver;
- `advcake` — для ADV.Cake;
- `advmaker` — для Advmaker.ru;
- `aport (aport.ru)` — для Апорт;
- `AvitoPromo` — для Avito Промо;
- `begun` — для Begun;
- `bing` — для Bing Ads;
- `B2BContext` — для B2BContext;
- `city_ads` — для CityAds Media;
- `criteo` — для Criteo;
- `directadvert (directadvert.ru)` — для Direct/ADVERT;
- `drivenetwork` — для DriveNetwork;
- `epn, epnbz` — для E.PN;
- `facebook (fb, facebook.com, fb.com)` — для Facebook***;
- `flocktory` — для Flocktory;
- `gdeslon, gdeslon_cpa` — для Где Слон?;
- `giraffio` — для giraffe.io (AppCity);
- `google (adwords, adsense)` — для Google;
- `instagram` — для Instagram***;
- `kavanga` — для Каванга;
- `ladycenter` — Ladycenter;
- `link` — для ЛинкРУ;
- `magna` — для Magna Context;
- `marketgid` — для МаркетГид;
- `medialand` — для Medialand;
- `merchant` — для Google Merchant;
- `moimir` — для Мой мир Mail.ru;
- `nnn (nnn.ru)` — для NNN (National News Network);
- `odnoklassniki` — для Одноклассники;
- `ozon` — для Ozon;
- `perfluence` — для Perfluence;
- `price (price.ru, priceru, price-gmc)` — для Price.ru;
- `prre` — для PRRE.RU;
- `rtbhouse` — для RTB House;
- `mytarget (targetmailru)` — для myTarget (Target Mail.ru);
- `taboola` — для Taboola;
- `tiktok` — для TikTok;
- `torg.mail.ru` — для Товары Mail.ru;
- `trorer (rorer)` — для RORER;
- `Ttarget` — для tTarget;
- `videonow` — для Videonow.ru;
- `vkontakte (vk, vk.com)` — для ВКонтакте;
- `vk_ads, vkads, vk-ads, vkr` — для VK Реклама;
- `whisla` — для Whisla;
- `youtube` — для YouTube.

Для отслеживания переходов с email-рассылок используйте значение `email` или `e-mail`, указывайте его в качестве параметра `openstat_service` или `openstat_source`.

Пример:

```
https://example.com/?from=transition-source
```

Для отслеживания переходов с email-рассылок используйте значение `email` или `e-mail`.

## ru/general/source-tags#reportОтображение меток в отчетах

Данные по меткам сортируются соответственно порядку расположения группировок на странице отчета двумя способами:

### ru/general/source-tags#uznajte-bolsheУзнайте больше

- [Как Метрика определяет источник трафика](ru/general/sources-tracking)
- [О группе отчетов «Метки»](ru/reports/tags)
- [Как решить проблему с UTM-метками](https://yandex.ru/blog/metrika-club/problemy-s-metkami-utm)

## ru/general/source-tags#qandaВопросы и ответы

**Значения, передаваемые в UTM-метках, регистрозависимые?**

* Сервис, запрещенный на территории РФ.

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

Сервис, запрещенный на территории РФ.

Параметр URL, который обрабатывается Метрикой по специальному алгоритму. Он не отображается в отчете Параметры URL, а по умолчанию отображается в [специальных отчетах](https://yandex.ru/support/metrica/reports/tags.html#tags). Это позволяет создавать более понятные и глубокие аналитические срезы.

### Была ли статья полезна?
