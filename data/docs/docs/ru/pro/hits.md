> Источник: https://yandex.ru/support/metrica/ru/pro/hits
# Список выгружаемых полей данных — хиты (события)

| Поле | Тип | Описание |
| --- | --- | --- |
| WatchID | UInt64 | Идентификатор хита |
| pageViewID | UInt32 | Идентификатор просмотра, в рамках которого произошло событие |
| VisitID | UInt64 | Идентификатор визита (доступно с 10 октября 2025 года) |
| HitVersion | UInt32 | Версия хита |
| Sign | Int8 | Признак статуса записи в инкрементальном логе |
| EventDate | Date | Дата хита |
| UTCEventTime | DateTime | Дата и время в формате UTC |
| Title | String | Заголовок страницы |
| CounterID | UInt32 | Идентификатор счетчика |
| ClientIP | UInt32 | IPv4 с которого было установлено TCP соединение с сервером |
| ClientIP6 | FixedString(16) | IPv6 с которого было установлено TCP соединение с сервером |
| RegionID | UInt32 | Идентификатор региона посетителя |
| OS | UInt32 | Идентификатор операционной системы посетителя (детально) |
| UserAgent | UInt32 | Идентификатор браузера посетителя |
| URL | String | Адрес страницы |
| Referer | String | Реферер |
| ResolutionWidth | UInt16 | Ширина экрана |
| ResolutionHeight | UInt16 | Высота экрана |
| ResolutionDepth | UInt8 | Глубина разрешения |
| UserAgentMajor | UInt16 | Старшая цифра версии браузера |
| CookieEnable | UInt8 | Признак включения cookies |
| JavascriptEnable | UInt8 | Признак включения JavaScript |
| IsMobile | UInt8 | Значение: 1, если хит совершен с мобильного браузера (на основании User Agent) |
| IsTablet | UInt8 | Хит совершен с браузера на планшете |
| MobilePhoneModel | String | Полное название модели мобильного телефона |
| TraficSourceID | Int8 | Идентификатор источника трафика |
| SearchEngineID | UInt16 | Идентификатор поисковой системы (детально) |
| AdvEngineID | UInt8 | Идентификатор рекламной системы |
| Experiment.SystemID | Array(Integer) | Массив идентификаторов вариантов экспериментов Varioqub . Варианты привязываются к визитам посетителей, которые попали в выборку. Стоит учитывать только положительные значения. Отрицательные значения — технические |
| IsArtifical | UInt8 | Искусственный хит, совершенный с помощью функции hit(), event() и пр. |
| WindowClientWidth | UInt16 | Ширина окна клиента |
| WindowClientHeight | UInt16 | Высота окна клиента |
| ClientTimeZone | Int16 | Временная зона на клиенте |
| PageCharset | String | Кодировка страницы сайта |
| IsLink | UInt8 | Хит является переходом по ссылке |
| IsDownload | UInt8 | Хит является загрузкой файла |
| IsNotBounce | UInt8 | Специальное событие не-отказ, для точного показателя отказов |
| IsParameter | UInt8 | Признак наличия параметра у хита. Не позволяет определить наличие пустых параметров у хита |
| BrowserLanguage | FixedString(2) | Язык, установленный в браузере |
| BrowserCountry | FixedString(2) | Страна, установленная в браузере |
| HTTPError | UInt16 | Код ошибки |
| SocialSourceNetworkID | UInt8 | Идентификатор социальной сети, с которой совершен переход |
| SocialSourceNetworkStrID | String | Строковый идентификатор социальной сети, с которой был переход |
| SocialSourcePage | String | Страница социальной сети, с которой совершен переход |
| GoalsReached | Array(UInt32) | Идентификаторы достигнутых целей, включая офлайн-конверсии, которые доступны с 12 августа 2025 года |
| OpenstatServiceName | String | Имя openstat-метки, рекламная площадка |
| OpenstatCampaignID | String | Идентификатор рекламной кампании openstat |
| OpenstatAdID | String | Идентификатор рекламы openstat |
| OpenstatSourceID | String | Тип рекламы openstat |
| UTMSource | String | Имя UTM-метки, рекламная площадка |
| UTMMedium | String | Тип рекламы UTM |
| UTMCampaign | String | Название рекламной кампании UTM |
| UTMContent | String | Дополнительная информация по UTM |
| UTMTerm | String | Ключевая фраза UTM |
| FromTag | String | Значение from из URL |
| HasGCLID | UInt8 | Признак наличия метки adWords (Google Click ID) |
| GCLID | String | Метка adWords (Google Click ID) |
| CLID | UInt32 | Параметр URL clid |
| HasSBCLID | UInt8 | Признак наличия метки SBCLID |
| SBCLID | String | Метка SBCLID |
| ShareService | String | Кнопка «Поделиться», имя сервиса |
| ShareURL | String | Кнопка «Поделиться», URL |
| ShareTitle | String | Кнопка «Поделиться», заголовок страницы |
| EAction.ProductName | Array(String) | Название товара (доступно с 19 июня 2025 года) |
| EAction.ProductID | Array(String) | Идентификатор или код товара (доступно с 19 июня 2025 года) |
| EAction.ProductDiscount | Array(String) | Размер скидки на товар (доступно с 19 июня 2025 года) |
| EAction.ProductList | Array(String) | Список, в который входят товары, связанные с транзакцией (доступно с 19 июня 2025 года) |
| EAction.ProductBrand | Array(String) | Бренд, к которому относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory | Array(String) | Категория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory1 | Array(String) | Подкатегория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory2 | Array(String) | Подкатегория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory3 | Array(String) | Подкатегория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory4 | Array(String) | Подкатегория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductCategory5 | Array(String) | Подкатегория, к которой относится товар (доступно с 19 июня 2025 года) |
| EAction.ProductVariant | Array(String) | Вариант товара (доступно с 19 июня 2025 года) |
| EAction.ProductPosition | Array(Int32) | Позиция товара в списке или коллекции (доступно с 19 июня 2025 года) |
| EAction.ProductPrice | Array(Int64) | Цена товара (доступно с 19 июня 2025 года) |
| EAction.ProductCurrency | Array(String) | Валюта товара (доступно с 19 июня 2025 года) |
| EAction.ProductCoupon | Array(String) | Код купона, связанного с товаром (доступно с 19 июня 2025 года) |
| EAction.ProductQuantity | Array(Int64) | Количество единиц товара |
| EAction.Type | Array(UInt8) | Тип события: 10 - Просмотр списка товаров 6 - Клик по товару 1 - Просмотр карточки товара 4 - Добавление товара в корзину 5 - Удаление товара из корзины 3 - Оформление заказа (доступно с 19 июня 2025 года) |
| EAction.ProductCurrencyID | Array(UInt16) | Код валюты товара (доступно с 19 июня 2025 года) |
| EPromotion.ID | Array(String) | Идентификатор промокампании (доступно с 19 июня 2025 года) |
| EPromotion.Name | Array(String) | Название промокампании (доступно с 19 июня 2025 года) |
| EPromotion.Creative | Array(String) | Название рекламного баннера (доступно с 19 июня 2025 года) |
| EPromotion.CreativeSlot | Array(String) | Слот рекламного баннера (доступно с 19 июня 2025 года) |
| EPromotion.Position | Array(String) | Позиция рекламного баннера (доступно с 19 июня 2025 года) |
| EPromotion.Type | Array(UInt8) | Тип события 1 — просмотр 2 — клик (доступно с 19 июня 2025 года) |
| EPurchase.ID | Array(String) | Идентификатор транзакции (доступно с 19 июня 2025 года) |
| EPurchase.Affiliation | Array(String) | Магазин или филиал, в котором произошла транзакция (доступно с 19 июня 2025 года) |
| EPurchase.Revenue | Array(Int64) | Общий доход или суммарная ценность транзакции (доступно с 19 июня 2025 года) |
| EPurchase.Tax | Array(Int64) | Сумма всех налогов, связанных с транзакцией (доступно с 19 июня 2025 года) |
| EPurchase.Shipping | Array(Int64) | Стоимость доставки, связанная с транзакцией (доступно с 19 июня 2025 года) |
| EPurchase.Coupon | Array(String) | Купон, погашенный при транзакции (доступно с 19 июня 2025 года) |
| EPurchase.Currency | Array(String) | Валюта транзакции (доступно с 19 июня 2025 года) |
| EPurchase.CurrencyID | Array(UInt16) | Код валюты транзакции (доступно с 19 июня 2025 года) |
| EPurchase.ProductQuantity | Array(Int64) | Количество единиц товара (доступно с 19 июня 2025 года) |
| ecommerce | String | События электронной коммерции |
| CallTalkDuration | UInt32 | Продолжительность разговора в секундах |
| CallHoldDuration | UInt32 | Продолжительность ожидания в секундах |
| CallMissed | UInt8 | Признак пропущенного звонка |
| CallFirstTimeCaller | UInt8 | Признак первого звонка от этого клиента |
| CallTag | String | Метки, ассоциированные со звонком |
| CallURL | String | Страница, с которой позвонили |
| CallTrackerURL | String | URL колл-трекера |
| OfflineUploadingID | UInt64 | Идентификатор загрузки офлайн-конверсии |
| params | String | Параметры |
| ParsedParams.Key1 | Array(String) | Параметр, уровень 1 |
| ParsedParams.Key2 | Array(String) | Параметр, уровень 2 |
| ParsedParams.Key3 | Array(String) | Параметр, уровень 3 |
| ParsedParams.Key4 | Array(String) | Параметр, уровень 4 |
| ParsedParams.Key5 | Array(String) | Параметр, уровень 5 |
| ParsedParams.Key6 | Array(String) | Параметр, уровень 6 |
| ParsedParams.Key7 | Array(String) | Параметр, уровень 7 |
| ParsedParams.Key8 | Array(String) | Параметр, уровень 8 |
| ParsedParams.Key9 | Array(String) | Параметр, уровень 9 |
| ParsedParams.Key10 | Array(String) | Параметр, уровень 10 |
| ParsedParams.Quantity | Array(UInt32) | Число параметров |
| DevicePixelRatio | Float32 | Пиксельное соотношение |
| BrowserEngineID | UInt8 | Идентификатор движка браузера |
| BrowserEngineVersion1 | UInt16 | Версия движка браузера |
| BrowserEngineVersion2 | UInt16 | Версия движка браузера |
| BrowserEngineVersion3 | UInt16 | Версия движка браузера |
| BrowserEngineVersion4 | UInt16 | Версия движка браузера |
| IsTV | UInt8 | Хит совершен с браузера на ТВ |
| DirectCLID | UInt64 | Идентификатор рекламного клика Директа. YCLID |
| IsIFrame | UInt8 | Признак хита из iframe |
| ClientID | UInt64 | Доменная кука и ClientID (значение, отправленное через Measurement Protocol ) |
| FirstPartyCookie | UInt64 | Доменная кука |
| MobilePhoneVendor | UInt16 | Производитель мобильного телефона |
| OriginalURL | String | Полный URL, если он был обрезан |
| NetworkType | UInt8 | Идентификатор типа соединения |
| UserAgentVersion2 | UInt32 | Полная версия браузера, число 2 |
| UserAgentVersion3 | UInt32 | Полная версия браузера, число 3 |
| UserAgentVersion4 | UInt32 | Полная версия браузера, число 4 |
| RecommendationSystemID | UInt8 | Идентификатор рекомендательной системы |
| MessengerID | UInt8 | Идентификатор мессенджера |
| OSFamily | String | Тип операционной системы |
| OSName | String | Название операционной системы |
| YQRID | String | Уникальная метка, которую проставляет Яндекс QR-генератор |
| QRCodeProviderID | UInt16 | Идентификатор провайдера QR-кодов |
| IsPageView | UInt8 | Хит является просмотром страницы |
| OSStr | String | Строковый идентификатор операционной системы посетителя (детально) |
| OSRoot | UInt8 | Идентификатор группы операционной системы посетителя |
| OSRootStr | String | Строковый идентификатор группы операционной системы посетителя |
| UserAgentStr | String | Строковый идентификатор браузера посетителя |
| TrafficSourceStrID | String | Строковый идентификатор источника трафика |
| SearchEngineStrID | String | Строковый идентификатор поисковой системы (детально) |
| SearchEngineRootID | UInt16 | Идентификатор поисковой системы |
| SearchEngineRootStrID | String | Строковый идентификатор поисковой системы |
| AdvEngineStrID | String | Строковый идентификатор рекламной системы |
| BrowserEngineStrID | String | Строковый идентификатор движка браузера |
| MobilePhoneVendorStr | String | Строковый идентификатор мобильного телефона |
| NetworkTypeStr | String | Строковый идентификатор типа соединения |
| RecommendationSystemStrID | String | Строковый идентификатор рекомендательной системы |
| MessengerStrID | String | Строковый идентификатор мессенджера |
| QRCodeProviderStrID | String | Строковый идентификатор провайдера QR-кодов |
| CounterUserIDHash | UInt64 | Идентификатор посетителя, сквозной в рамках одного счетчика, даже если он установлен на разных доменах |

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
