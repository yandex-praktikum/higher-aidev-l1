> Источник: https://yandex.ru/support/metrica/ru/ad/expenses
# Передача расходов

- [Передача расходов по источникам трафика](ru/ad/expenses#traffic-sources)
- [Интеграции Метрики для загрузки расходов на продвижение](ru/ad/expenses#integration)
- [Передача расходов с помощью CSV-файла специального формата](ru/ad/expenses#CSV-file)
- [Поля для передачи данных](ru/ad/expenses#CSV-file1)
- [Доступные значения TrafficSource и TrafficSourceDetail](ru/ad/expenses#values)

С помощью Метрики вы можете отслеживать эффективность любых источников трафика на вашем счетчике. Для этого можно передать в Метрику информацию о расходах по всем источникам трафика или по отдельным рекламным системам. Данные можно передавать:

- Через [сторонний сервис автоматизации](ru/ad/upload-connector).
- С помощью интеграций Метрики для загрузки расходов на продвижение.
- С помощью CSV-файла специального формата. Загрузка возможна в веб-интерфейсе Метрики и через [API](https://yandex.ru/dev/metrika/doc/api2/management/expenses/uploadbody-docpage/).

## ru/ad/expenses#traffic-sourcesПередача расходов по источникам трафика

Если источник трафика нельзя разметить UTM-метками или вам не требуется детализация рекламных расходов до отдельных кампаний, объявлений или типов размещения, вы все равно можете отправить расходы по такому источнику. Чтобы отправить расходы, укажите в загрузке расходов параметры `Источник` (`TrafficSource`) и `Источник трафика (детально)` (`TrafficSourceDetail`). Список значений этих параметров указан в [таблице](ru/ad/expenses#values).

Все интеграции Метрики для загрузки расходов на продвижение поддерживают автоматическую передачу источника трафика.

Чтобы посмотреть, какие метрики рассчитываются на основе загруженных данных и какие задачи вы сможете решить, перейдите в [отчет «Источники, расходы и ROI»](ru/sources/ad-expenses).

## ru/ad/expenses#integrationИнтеграции Метрики для загрузки расходов на продвижение

| Рекламная система | Как передавать данные | Примечание |
| --- | --- | --- |
| Директ | Данные передаются автоматически | Внимание Если вы самостоятельно загрузите расходы, они будут дублироваться с переданными автоматически и отчет станет некорректным. |
| myTarget | Настройте подключение в Метрике | Источником расходов будет указан Переходы по рекламе — myTarget |
| ВКонтакте | Настройте подключение в Метрике | Источником расходов будет указан Переходы по рекламе — Вконтакте |
| VK Реклама | Настройте подключение в Метрике | Источником расходов будет указан Переходы по рекламе — VK Реклама |
| Google Ads | Настройте подключение в Метрике | Источником расходов будет указан Переходы по рекламе — Google Ads |
| Facebook * Ads | Настройте подключение в Метрике | Источником расходов будет указан Переходы по рекламе — Facebook * . При наличии в UtmSource значения instagram — Переходы по рекламе — Instagram * |

## ru/ad/expenses#CSV-fileПередача расходов с помощью CSV-файла специального формата

Чтобы передавать данные о рекламной кампании в Метрику, сформируйте CSV-файл, подходящий под формат передачи расходов в Метрику.

[Пример файла для загрузки данных](https://download.cdn.yandex.net/from/yandex.ru/support/ru/metrica/files/expenses.csv)

## ru/ad/expenses#CSV-fileПоля для передачи данных

| Название поля | Обязательно | Описание | Пример |
| --- | --- | --- | --- |
| Date | Да | Период, за который передаются данные. Может быть день или отрезок времени. В формате Unix Time Stamp по стандарту ISO 8601 (YYYY-MM-DD). Чтобы указать диапазон дат, используйте / | 2020-02-18 2020-01-18/2020-02-18 |
| Expenses | Да | Сумма, которая была потрачена на рекламу без учета НДС | 50 000 |
| Currency | Нет | Трехбуквенный код валюты по ISO 4217 . Если валюта не указана, то для формирования отчетов Метрика использует валюту, которая указана в настройках счетчика | RUB |
| TrafficSource | Да * | Источник трафика первого уровня. Доступные значения описаны в таблице | ad |
| TrafficSourceDetail | Нет | Источник трафика второго уровня. Доступные значения описаны в таблице | vk |
| UTMSource | Да * | Значение UTM-метки, которое указано в URL ссылки в рекламном объявлении. Обратите внимание на регистр, в котором указано значение метки | vk |
| UTMCampaign | Нет | new |  |
| UTMMedium | Нет | cpc |  |
| UTMTerm | Нет | shirt-blue |  |
| UTMContent | Нет | shirt |  |
| Clicks | Нет | Количество кликов по рекламным объявлениям | 100 |

* Поле `UTMSource` обязательно, если не указано поле `TrafficSource`.

## ru/ad/expenses#valuesДоступные значения TrafficSource и TrafficSourceDetail

|  | TrafficSource | TrafficSourceDetail |
| --- | --- | --- |
| Внутренние переходы | internal | — |
| Прямые заходы | direct | — |
| Переходы по ссылкам на сайтах | referral | Укажите домен в формате site.ru |
| Переходы из поисковых систем | organic | Список значений |
| Переходы по рекламе | ad | Список значений |
| Переходы с сохраненных страниц | saved | — |
| Не определен | undefined | — |
| Переходы с почтовых рассылок | email | — |
| Переходы из социальных сетей | social | Список значений |
| Переходы из мессенджеров | messenger | Список значений |
| Переходы по QR-коду | qrcode | — |
| Переходы из рекомендательных систем | recommend | Список значений |

| Название | Идентификатор |
| --- | --- |
| Другая поисковая система: определено по меткам | unknown — сюда попадает все, что не относится к другим идентификаторам |
| Яндекс | yandex |
| Metabot.ru | metabot_ru |
| Poisk.ru | poisk_ru |
| blekko | blekko |
| Rx24 | rx24 |
| Gigabase | gigabase |
| AOL | aol_search |
| Дзен Новости | yandex_news |
| I.ua | i_ua |
| MyStart by IncrediMail.com | mystart |
| Winamp Search | winamp_search |
| Поиск на NUR.KZ | nur_kz |
| Topsy | topsy |
| KAZ.KZ | kaz_kz |
| All.by | all_by |
| Tut.by | tut_by |
| Webalta | webalta |
| Magna | magna |
| Lycos | lycos |
| Meta.ua | meta_ua |
| My Web Search | myweb_search |
| Exalead.fr | exalead_fr |
| Гювеч ( GBG.BG ) | gbg_bg |
| Conduit | conduit |
| Babylon Search | babylon_search |
| Alexa Web Search | alexa_web |
| search.1and1.com | 1and1 |
| 7search.com | 7search |
| search.about.com | about |
| acoon.com | acoon |
| Alhea | alhea |
| AltaVista | altavista |
| amfibi.com | amfibi |
| Aport | aport |
| arama.com | arama |
| Ask.com | ask_com |
| search.avg.com | avg |
| Baidu | baidu |
| biglobe.ne.jp | biglobe_ne |
| Bigmir.net | bigmir_net |
| Bing | bing |
| Coc Coc | coccoc |
| crawler.com | crawler |
| Cuil.com | cuil_com |
| DAEMON search | daemon_search |
| daum.net | daum |
| dogpile.com | dogpile |
| DuckDuckGo | duckduckgo |
| Ecosia | ecosia |
| finnerask.com | finnerask |
| start.funmoods.com | funmoods |
| ГДЕ.РУ | gde_ru |
| gigablast.com | gigablast |
| gmx.net | gmx_net |
| GoGo | gogo |
| goo.ne.jp | goo_ne |
| Google | google |
| hakia.com | hakia |
| search.handycafe.com | handycafe |
| hi.ru | hi_ru |
| hotbot.com | hotbot |
| Hotline.ua | hotline |
| icerocket.com | icerocket |
| Поиск на ICQ.com | icq_search |
| search.iminent.com | iminent |
| search.incredibar.com | incredibar |
| infospace.com | infospace |
| istella.it | istella |
| k9safesearch | k9safesearch |
| Поиск KM.RU | km_search |
| kvasir.no | kvasir |
| Liveinternet | liveinternet |
| Live Search | livesearch |
| Mail.ru | mail_ru |
| mamma.com | mamma |
| metacrawler.com | metacrawler |
| MSN | msn |
| myahint.com | myahint |
| najdi.si | najdi_si |
| naver.com | naver |
| netsearch.org | netsearch |
| Nigma | nigma |
| onet.pl | onet_pl |
| Pivim.com | pivim_com |
| plusnetwork.com | plusnetwork |
| Поиск на QIP.ru | qip_search |
| Quintura | quintura |
| Qwant | qwant |
| Rambler | rambler |
| sapo.pt | sapo_pt |
| scrubtheweb.com | scrubtheweb |
| search.gmx.net | search_gmx_net |
| searchcompletion.com | searchcompletion |
| search-results.com | searchresults |
| searchya.com | searchya |
| Seznam | seznam |
| Skydns | skydns |
| search.smilebox.com | smilebox |
| so.360.cn | so360 |
| search.softonic.com | softonic |
| Sogou | sogou |
| speedbit.com | speedbit |
| Спутник | sputnik |
| Startpagina | startpagina |
| startsiden.no/sok | startsiden_no |
| search.sweetim.com | sweetim |
| Ukr.net | ukr_net |
| v9.com | v9 |
| virgilio.it | virgilio_it |
| voila.fr | voila |
| Web.de | web_de |
| Wikia Search | wikia_search |
| wow | wow |
| wp.pl | wp_pl |
| Yaani | yaani |
| Yahoo! | yahoo |
| yam.com | yam |
| yippy.com | yippy |
| Zapmeta | zapmeta |

| Название | Идентификатор |
| --- | --- |
| Google Ads | google_adwords |
| Бегун | begun |
| Красноярск.Биз | krasnoyarsk_biz |
| Линк.ру | link_ru |
| MadBanner | madbanner |
| Magna-context | magna_context |
| RORER | rorer |
| Ставка.ру | stavka_ru |
| Вебальта | webalta |
| Маркет | market |
| aVtomarket.ru | avtomarket |
| Каванга | kavanga |
| PRRE.RU | prre |
| Videonow.ru | videonow |
| AdRiver | adriver |
| AdFox | adfox |
| MediaTarget | mediatarget |
| DirectPoint | directpoint |
| TBN | tbn |
| LitBN | litbn |
| SoftBN | softbn |
| AdLand | adland |
| Linkad | linkad |
| Украинская Баннерная Сеть | banner |
| БаннерБанк | banner_bank |
| BannerHost | banner_host |
| List Banner Exchange | list_banner_exchange |
| Pravda Banner Network | pravda_banner_network |
| Land Banner Network | land_banner_network |
| IBN | ibn |
| BigBN | bigbn |
| Медийная реклама | media_awaps |
| AdvMaker.ru | advmaker |
| Товары@Mail.Ru | tovary_mail_ru |
| ВКонтакте | vkontakte |
| Facebook * | facebook |
| Одноклассники | odnoklassniki |
| Мой мир | moimir |
| B2BContext | b2bcontext |
| B2BCAdNewsontext | adnews |
| People Group | people_group |
| VisitWeb.com | visitweb |
| Adlabs Media Network | adlabs_media_network |
| Admitad | admitad |
| Medialand | medialand |
| MyTarget | target_mail_ru |
| Апорт | aport |
| Price.ru | price_ru |
| МаркетГид | marketgid |
| adPremium | adpremium |
| ExoClick | exoclick |
| LadyCenter | ladycenter |
| POST RMBN | POST RMBN |
| Direct/ADVERT | directadvert |
| Recreativ | recreativ |
| AdWolf | adwolf |
| Adonweb | adonweb |
| AdBlender | adblender |
| AdvertLink | advertlink |
| SharedAdDomain | sharedaddomain |
| Adnxs | Adnxs |
| Targetix | targetix |
| adhood | adhood |
| Criteo | criteo |
| Google Merchant | google_merchant |
| Avito Контекст | avito_context |
| Sociomantic | sociomantic |
| Ttarget | ttarget |
| Яндекс: Дисплей | display |
| Avito Промо | avito_promo |
| Рекламная сеть Яндекса: блоки RTB | yandexrtb |
| ADNOUS | adnous |
| VigLink | viglink |
| Instagram * | instagram |
| Раре.Ру | rareru |
| BingAds | bingads |
| Whisla | whisla |
| Taboola | taboola |
| Другая реклама: определено по меткам | unknown |
| YouTube | youtube |
| Giraff.io | giraffio |
| DriveNetwork | drivenetwork |
| NNN | nnn |
| Nadavi | nadavi |
| Tkat.ru | tkat |
| coccoc | coccoc |
| relap | relap |
| TikTok | tiktok |
| Яндекс ПромоСтраницы | zen_ads |
| RTB House | rtbhouse |
| Yandex: Direct | yandex_direct_star |
| VK Реклама | vk_ads |
| Ozon | ozon |

| Название | Идентификатор |
| --- | --- |
| ВКонтакте | vk |
| Twitter | twitter |
| Facebook * | facebook |
| Одноклассники | odnoklassniki |
| Liveinternet | liveinternet |
| Livejournal | livejournal |
| Лепрозорий | leprosorium |
| Diary.ru | diary |
| Google+ | google |
| Мой Мир@Mail.Ru | mail |
| ORKUT | orkut |
| Я.ру | ya |
| Мой Круг | moikrug |
| в Кругу Друзей | vkrugudruzei |
| Linked in | linkedin |
| juick | juick |
| connect.ua | connect |
| LJ.Rossia.org | rossia |
| FriendFeed | friendfeed |
| myspace.com | myspace |
| delicious.com | delicious |
| Привет!ру | privet |
| www.draugiem.lv | draugiem |
| cloob.com | cloob |
| mixi | mixi |
| hi.baidu.com | baidu |
| hi5.com | hi5 |
| renren.com | renren |
| skyrock.com | skyrock |
| tumblr.com | tumblr |
| Instagram * | instagram |
| sprashivai.ru | sprashivai |
| ask.fm | ask |
| Pinterest | pinterest |
| Постила | postila |
| Фотострана | fotostrana |
| Reddit | reddit |
| pin.me | pin |
| point.im | point |
| StumbleUpon | adnews |
| Другая социальная сеть: определено по меткам | unknown — сюда попадает все, что не относится к другим идентификаторам |
| YouTube | youtube |

| Название | Идентификатор |
| --- | --- |
| Другой мессенджер: определено по меткам | unknown — сюда попадает все, что не относится к другим идентификаторам |
| Telegram | telegram |
| WhatsApp | whatsapp |
| Viber | viber |
| Skype | skype |
| WeChat | wechat |
| Яндекс.Мессенджер | yandex_chats |
| Facebook * | facebook |
| ВКонтакте | vk |

| Название | Идентификатор |
| --- | --- |
| Другая рекомендательная система: определено по меткам | unknown — сюда попадает все, что не относится к другим идентификаторам |
| Дзен | zen_yandex |
| Google Discover | google_discover |
| Opera Personal News | opera_news |
| Sony News Suite | sony_news |
| Flipboard | flipboard |
| Pulse | pulse |
| Мир тесен | mirtesen |
| Toutiao | toutiao |
| Рамблер | rambler |

Примечание

Загрузить данные можно за последние 360 дней и не более чем на 30 дней вперед.

Передавать CSV-файл с данными можно:

1. Перейдите в Метрику на страницу **Настройка** → **Загрузка данных.**
2. В блоке **Расходы на рекламу** нажмите **Загрузить**.
3. Загрузите подготовленный файл.
4. В появившемся окне укажите: значения полей `TrafficSource` и `TrafficSourceDetail`; значение метки `UTMSource` (рекламную систему, из которой был выгружен файл). Убедитесь, что регистр, в котором указано значение UTM-метки, совпадает с регистром в URL рекламного объявления. столбец в файле, который соответствует полю `Дата`. столбец в файле, который соответствует полю `Расходы`. Выберите тип разделителя суммы, который используется в выгруженном в шаге 1 файле — запятую или точку. столбец в файле, который соответствует полю `Клики`. валюту, в которой указаны расходы. Если валюта не указана, для формирования отчетов Метрика использует валюту, из настроек счетчика. другие UTM-метки и их значения из списка. Вы можете вписать одно значение для всех меток. Например, для метки `UTMMedium` можно указать значение `cpc`.
5. Нажмите **Загрузить данные**.

[Документация к API Метрики](https://yandex.ru/dev/metrika/doc/api2/management/expenses/uploadbody-docpage/)

Если вы повторно загружаете файл с данными за один и тот же период, новый файл заменит ранее загруженный.

Если в файле указан отрезок времени, то Метрика равномерно распределит в нем числовые значения (например расход, количество кликов и пр.) для отображения в отчете.

* Сервис, запрещенный на территории РФ.

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

Сервис, запрещенный на территории РФ.

* Поле `UTMSource` обязательно, если не указано поле `TrafficSource`.

### Была ли статья полезна?
