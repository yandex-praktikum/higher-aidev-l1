> Источник: https://yandex.ru/support/metrica/ru/pro/visits
# Список выгружаемых полей данных — визиты

Примечание

Потоковая передача подразумевает изменение данных в визитах по мере поступления новых событий, поэтому в выгружаемых данных будут разные версии одного визита. Это нужно учитывать при построении аналитики.

| Поле | Тип | Описание |
| --- | --- | --- |
| CounterID | UInt32 | Идентификатор счетчика |
| StartDate | Date | Дата начала визита |
| Sign | Int8 | Признак статуса записи в инкрементальном логе |
| VisitID | UInt64 | Идентификатор визита, уникален в рамках одного года |
| Duration | UInt32 | Длительность визита в секундах |
| UTCStartTime | DateTime | Timestamp начала визита |
| PageViews | Int32 | Просмотры |
| IsBounce | UInt8 | Является ли визит отказом |
| Referer | String | Реферер |
| StartURL | String | URL, с которого начался визит |
| EndURL | String | URL, на котором закончился визит |
| LinkURL | String | URL внешней ссылки, если по ней был переход |
| MobilePhoneModel | String | Полное название модели мобильного телефона |
| ClientIP | UInt32 | IPv4, с которого было установлено TCP соединение с сервером |
| ClientIP6 | FixedString(16) | IPv6, с которого было установлено TCP соединение с сервером |
| ResolutionWidth | UInt16 | Ширина экрана |
| ResolutionHeight | UInt16 | Высота экрана |
| UserAgentMajor | UInt16 | Старшая цифра версии браузера |
| WindowClientWidth | UInt16 | Ширина окна клиента |
| WindowClientHeight | UInt16 | Высота окна клиента |
| ClientTimeZone | Int16 | Временная зона на клиенте |
| DevicePixelRatio | Float32 | Пиксельное соотношение (коэффициент зумирования) |
| OS | UInt32 | Операционная система посетителя |
| UserAgent | UInt32 | Браузер посетителя |
| ResolutionDepth | UInt8 | Глубина цвета |
| CookieEnable | UInt8 | Включены ли куки |
| JavascriptEnable | UInt8 | Признак включения JavaScript |
| IsMobile | UInt8 | Признак мобильного браузера |
| IsTablet | UInt8 | Признак планшета |
| BrowserLanguage | UInt16 | Язык, установленный в браузере |
| BrowserCountry | UInt16 | Страна, установленная в браузере |
| BrowserEngineID | UInt8 | Идентификатор движка браузера |
| BrowserEngineVersion1 | UInt16 | Версия движка браузера |
| BrowserEngineVersion2 | UInt16 | Версия движка браузера |
| BrowserEngineVersion3 | UInt16 | Версия движка браузера |
| BrowserEngineVersion4 | UInt16 | Версия движка браузера |
| Goals.ID | Array(UInt32) | Идентификатор целей, достигнутых за этот визит |
| Goals.Serial | Array(UInt32) | Порядковые номера достижений цели с конкретным идентификатором |
| Goals.EventTime | Array(DateTime) | Время достижения каждой цели |
| Goals.Price | Array(Int64) | Ценность цели |
| Goals.OrderID | Array(String) | Идентификатор заказов |
| Goals.CurrencyID | Array(UInt32) | Идентификатор валюты |
| Goals.CallTalkDuration | Array(UInt32) | Продолжительность разговора в секундах |
| Goals.CallHoldDuration | Array(UInt32) | Продолжительность ожидания в секундах |
| Goals.CallMissed | Array(UInt32) | Признак пропущенного звонка |
| Goals.CallFirstTimeCaller | Array(UInt32) | Признак первого звонка от этого клиента |
| Goals.CallTag | Array(String) | Метки, ассоциированные со звонком |
| Goals.CallURL | Array(String) | Страница, с которой позвонили |
| Goals.CallTrackerURL | Array(String) | URL колл-трекера |
| WatchIDs | Array(UInt64) | Хиты, которые были в этом визите, кроме параметров визитов |
| FirstVisit | DateTime | Время и дата первого визита посетителя |
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
| HasGoalReachesOverflow | UInt8 | Количество целей в визите или их объем больше максимально допустимого значения |
| IsTV | UInt8 | Визит совершен с телевизора или нет |
| EPromotion.ID | Array(String) | Идентификатор промокампании |
| EPromotion.Name | Array(String) | Название промокампании |
| EPromotion.Creative | Array(String) | Название рекламного баннера |
| EPromotion.CreativeSlot | Array(String) | Слот рекламного баннера |
| EPromotion.Position | Array(String) | Позиция рекламного баннера |
| EPromotion.URL | Array(String) | Адрес страницы, на которой произошло событие |
| EPromotion.EventTime | Array(DateTime) | Время наступления события |
| EPromotion.Type | Array(UInt8) | Тип события, произошедшего с промокампанией, где 1 — просмотр, 2 — клик |
| EPurchase.ID | Array(String) | Идентификатор транзакции |
| EPurchase.EventTime | Array(DateTime) | Время транзакции |
| EPurchase.Affiliation | Array(String) | Магазин или филиал, в котором произошла транзакция |
| EPurchase.Revenue | Array(Int64) | Общий доход или суммарная ценность транзакции |
| EPurchase.Tax | Array(Int64) | Сумма всех налогов, связанных с транзакцией |
| EPurchase.Shipping | Array(Int64) | Стоимость доставки, связанная с транзакцией |
| EPurchase.Coupon | Array(String) | Купон, погашенный при транзакции |
| EPurchase.Currency | Array(String) | Валюта транзакции |
| EPurchaseOverflow | UInt8 | Количество элементов в массиве EPurchase.ID больше максимально допустимого значения |
| EPurchase.CurrencyID | Array(UInt16) | Код валюты транзакции |
| EPurchase.ProductQuantity | Array(Int64) | Количество единиц товара |
| EPurchaseWithProducts.ID | Array(String) | Идентификатор транзакции |
| EPurchaseWithProducts.ProductDiscount | Array(String) | Размер скидки на товар в заказе |
| EPurchaseWithProducts.EventTime | Array(DateTime) | Время транзакции |
| EPurchaseWithProducts.Affiliation | Array(String) | Магазин или филиал, в котором произошла транзакция |
| EPurchaseWithProducts.Revenue | Array(Int64) | Общий доход или суммарная ценность транзакции |
| EPurchaseWithProducts.Tax | Array(Int64) | Сумма всех налогов, связанных с транзакцией |
| EPurchaseWithProducts.Shipping | Array(Int64) | Стоимость доставки, связанная с транзакцией |
| EPurchaseWithProducts.Coupon | Array(String) | Купон, погашенный при транзакции |
| EPurchaseWithProducts.ProductID | Array(String) | Идентификатор или код товара |
| EPurchaseWithProducts.ProductName | Array(String) | Название товара |
| EPurchaseWithProducts.ProductList | Array(String) | Список, в который входят товары, связанные с транзакцией |
| EPurchaseWithProducts.ProductBrand | Array(String) | Бренд, к которому относится товар |
| EPurchaseWithProducts.ProductCategory | Array(String) | Категория, к которой относится товар |
| EPurchaseWithProducts.ProductCategory1 | Array(String) | Подкатегория, к которой относится товар |
| EPurchaseWithProducts.ProductCategory2 | Array(String) | Подкатегория, к которой относится товар |
| EPurchaseWithProducts.ProductCategory3 | Array(String) | Подкатегория, к которой относится товар |
| EPurchaseWithProducts.ProductCategory4 | Array(String) | Подкатегория, к которой относится товар |
| EPurchaseWithProducts.ProductCategory5 | Array(String) | Подкатегория, к которой относится товар |
| EPurchaseWithProducts.ProductVariant | Array(String) | Вариант товара |
| EPurchaseWithProducts.ProductPosition | Array(Int32) | Позиция товара в списке или коллекции |
| EPurchaseWithProducts.ProductPrice | Array(Int64) | Цена товара |
| EPurchaseWithProducts.ProductCurrency | Array(String) | Валюта товара |
| EPurchaseWithProducts.ProductCoupon | Array(String) | Код купона, связанного с товаром |
| EPurchaseWithProducts.Quantity | Array(Int64) | Количество единиц товара |
| EPurchaseWithProductsOverflow | UInt8 | Факт достижения лимита по EPurchaseWithProducts |
| EPurchaseWithProducts.Currency | Array(String) | Валюта товара |
| EPurchaseWithProducts.CurrencyID | Array(UInt16) | Код валюты товара |
| EPurchaseWithProducts.ProductCurrencyID | Array(UInt16) | Код валюты товара |
| EAction.ProductName | Array(String) | Название товара |
| EAction.ProductID | Array(String) | Идентификатор или код товара |
| EAction.ProductDiscount | Array(String) | Размер скидки на товар |
| EAction.ProductList | Array(String) | Список, в который входят товары, связанные с транзакцией |
| EAction.ProductBrand | Array(String) | Бренд, к которому относится товар |
| EAction.ProductCategory | Array(String) | Категория, к которой относится товар |
| EAction.ProductCategory1 | Array(String) | Подкатегория, к которой относится товар |
| EAction.ProductCategory2 | Array(String) | Подкатегория, к которой относится товар |
| EAction.ProductCategory3 | Array(String) | Подкатегория, к которой относится товар |
| EAction.ProductCategory4 | Array(String) | Подкатегория, к которой относится товар |
| EAction.ProductCategory5 | Array(String) | Подкатегория, к которой относится товар |
| EAction.ProductVariant | Array(String) | Вариант товара |
| EAction.ProductPosition | Array(Int32) | Позиция товара в списке или коллекции |
| EAction.ProductPrice | Array(Int64) | Цена товара |
| EAction.ProductCurrency | Array(String) | Валюта товара |
| EAction.ProductCoupon | Array(String) | Код купона, связанного с товаром |
| EAction.ProductQuantity | Array(Int64) | Количество единиц товара |
| EAction.EventTime | Array(DateTime) | Время события |
| EAction.Type | Array(UInt8) | Тип события Подробно Просмотр товара (detail). Изменение состояния корзины в рамках визита. Покупка товара. Добавление товара в корзину. Удаление товара из корзины. Клик по товару. Начало оформления заказа. Просмотр промокампании. Клик по промокампании. Просмотр списка товаров. |
| EAction.ProductCurrencyID | Array(UInt16) | Код валюты товара |
| EActionOverflow | UInt8 | Факт достижения лимита по EAction |
| ClientID | UInt64 | Доменная кука и ClientID (значение, отправленное через Measurement Protocol ) |
| FirstPartyCookie | UInt64 | Доменная кука |
| MobilePhoneVendor | UInt16 | Производитель мобильного телефона |
| NetworkType | UInt8 | Тип соединения |
| UserAgentVersion2 | UInt32 | Полная версия браузера, число 2 |
| UserAgentVersion3 | UInt32 | Полная версия браузера, число 3 |
| UserAgentVersion4 | UInt32 | Полная версия браузера, число 4 |
| VisitVersion | UInt32 | Версия визита |
| PublisherEvents.TraficSource | Array(Int8) | Источник трафика для статьи |
| PublisherEvents.EventID | Array(UInt64) | WatchID просмотра, к которому относится статья |
| PublisherEvents.PublicationTime | Array(DateTime) | Дата публикации статьи |
| PublisherEvents.ArticleID | Array(UInt32) | Идентификатор статьи |
| PublisherEvents.Title | Array(String) | Заголовок статьи |
| PublisherEvents.Rubric | Array(String) | Рубрика статьи |
| PublisherEvents.Rubric2 | Array(String) | Рубрика второго уровня для статьи |
| PublisherEvents.Topics | Array(Array(String)) | Тематики статьи |
| PublisherEvents.Authors | Array(Array(String)) | Авторы статьи |
| PublisherEvents.InvolvedTime | Array(UInt32) | Время, в течение которого посетитель видел статью |
| PublisherEvents.ScrollDown | Array(UInt8) | Показывает, насколько была проскроллена статья |
| PublisherEvents.Chars | Array(UInt32) | Число знаков в тексте статьи |
| PublisherEvents.ArticleHeight | Array(UInt32) | Высота статьи в пикселях |
| PublisherEvents.URLCanonical | Array(String) | Каноничный URL статьи |
| PublisherEvents.SearchEngineID | Array(UInt16) | Источник трафика для статьи — поисковая система |
| PublisherEvents.AdvEngineID | Array(UInt8) | Источник трафика для статьи — рекламная система |
| PublisherEvents.SocialSourceNetworkID | Array(UInt8) | Источник трафика для статьи — социальная сеть |
| PublisherEvents.ReferrerDomain | Array(String) | Источник трафика для статьи — домен реферера |
| PublisherEvents.ReferrerPath | Array(String) | Источник трафика для статьи — путь реферера |
| PublisherEvents.FromArticleID | Array(UInt32) | Идентификатор статьи, с которой перешли на текущую |
| PublisherEvents.HasRecircled | Array(UInt8) | Была ли рециркуляция с просмотра (перешел ли посетитель на другую статью на сайте) |
| PublisherEvents.HitEventTime | Array(DateTime) | Время хита |
| EAction.URL | Array(String) | URL у EAction события |
| PublisherEvents.RecommendationSystemID | Array(UInt8) | Источник трафика для статьи — рекомендательная система |
| PublisherEvents.MessengerID | Array(UInt8) | Источник трафика для статьи — мессенджер |
| PublisherEvents.TurboType | Array(Enum8) | Тип Турбо |
| OSFamily | String | Тип операционной системы |
| OSName | String | Название операционной системы |
| TrafficSource.Model | Array(Enum8) | Идентификатор типа атрибуции Возможные значения 1 — последний переход; 5 — последний значимый переход (кросс-девайс); 6 — первый переход (кросс-девайс); 11 — автоматическая. |
| TrafficSource.StartTime | Array(DateTime) | Дата и время начала визита |
| TrafficSource.ID | Array(Int8) | Идентификатор источника трафика Возможные значения -1 — внутренние переходы; 0 — прямые заходы; 1 — переходы по ссылкам на сайтах; 2 — переходы из поисковых систем; 3 — переходы по объявлениям; 4 — переходы с сохраненных страниц; 5 — не определен; 6 — переходы по внешним ссылкам; 7 — переходы с почтовых рассылок; 8 — переходы из соц. сетей; 9 — переходы из рекомендательных систем; 10 — переходы из мессенджеров; 11 — переходы по QR-коду. |
| TrafficSource.SearchEngineID | Array(UInt16) | Идентификатор поисковой системы (детально) |
| TrafficSource.SocialSourceNetworkID | Array(UInt8) | Идентификатор социальной сети, из которой был переход |
| TrafficSource.Domain | Array(String) | Переход с сайтов |
| TrafficSource.SocialSourcePage | Array(String) | Страница социальной сети, из которой был переход |
| TrafficSource.RecommendationSystemID | Array(UInt8) | Идентификатор рекомендательной системы |
| TrafficSource.MessengerID | Array(UInt8) | Идентификатор мессенджера |
| TrafficSource.OpenstatServiceName | Array(String) | Имя openstat метки, рекламная площадка |
| TrafficSource.OpenstatCampaignID | Array(String) | Идентификатор рекламной кампании openstat |
| TrafficSource.OpenstatAdID | Array(String) | Идентификатор рекламы openstat |
| TrafficSource.OpenstatSourceID | Array(String) | Тип рекламы openstat |
| TrafficSource.UTMSource | Array(String) | Значение utm_source |
| TrafficSource.UTMMedium | Array(String) | Значение utm_medium |
| TrafficSource.UTMCampaign | Array(String) | Значение utm_campaign |
| TrafficSource.UTMContent | Array(String) | Значение utm_content |
| TrafficSource.UTMTerm | Array(String) | Значение utm_term |
| TrafficSource.FromTag | Array(String) | Значение from из URL |
| TrafficSource.CLID | Array(UInt32) | Параметр урла clid |
| TrafficSource.DirectCLID | Array(UInt64) | Идентификатор рекламного клика Директа. YCLID |
| TrafficSource.HasGCLID | Array(UInt8) | Признак наличия метки adWords (Google CLick ID) |
| TrafficSource.GCLID | Array(String) | Метка adWords (Google CLick ID) |
| TrafficSource.HasSBCLID | Array(UInt8) | Признак наличия метки SBCLID |
| TrafficSource.SBCLID | Array(String) | Метка SBCLID |
| TrafficSource.ClickBannerID | Array(UInt64) | Идентификатор рекламного объявления |
| TrafficSource.AdvEngineID | UInt8 | Идентификатор рекламной системы |
| TrafficSource.ClickTargetType | Array(UInt16) | Площадка размещения |
| TrafficSource.ClickGroupBannerID | Array(UInt64) | Идентификатор группы объявлений Директа |
| TrafficSource.ClickDirectCampaignID | Array(UInt32) | Идентификатор кампании в Директе |
| CDPOrder.ID | Array(UInt64) | SipHash(toString(OrderID) |
| CDPOrder.UserID | Array(UInt64) | SipHash(toString(UserID) |
| CDPOrder.Version | Array(UInt32) | Версия заказа |
| CDPOrder.CreateTime | Array(DateTime) | Время создания заказа |
| CDPOrder.UpdateTime | Array(DateTime) | Время изменения заказа |
| CDPOrder.Revenue | Array(UInt64) | Загруженная посетителем стоимость заказа |
| CDPOrder.Cost | Array(UInt64) | Загруженная посетителем ценность заказа |
| CDPOrder.Status | Array(UInt8) | Статус заказа |
| CDPOrder.ProductNames | Array(Array(String)) | Названия товаров в заказе |
| CDPOrder.ProductQuantities | Array(Array(UInt32)) | Количества товаров в заказе |
| RegionID | UInt32 | Идентификатор региона посетителя |
| OSStr | String | Строковый идентификатор операционной системы посетителя (детально) |
| OSRoot | UInt8 | Идентификатор группы операционной системы посетителя |
| OSRootStr | String | Строковый идентификатор группы операционной системы посетителя |
| UserAgentStr | String | Строковый идентификатор браузера посетителя |
| BrowserEngineStrID | String | Строковый идентификатор движка браузера |
| EAction.TypeStr | Array(String) | Строковый идентификатор типа события |
| MobilePhoneVendorStr | String | Строковый идентификатор производителя мобильного телефона |
| NetworkTypeStr | String | Строковый идентификатор типа соединения |
| PublisherEvents.TrafficSourceStrID | Array(String) | Строковый идентификатор источника трафика для статьи |
| PublisherEvents.SearchEngineStrID | Array(String) | Строковый идентификатор источника трафика для статьи — поисковая система |
| PublisherEvents.AdvEngineStrID | Array(String) | Строковый идентификатор источника трафика для статьи — рекламная система |
| PublisherEvents.SocialSourceNetworkStrID | Array(String) | Строковый идентификатор источника трафика для статьи — социальная сеть |
| PublisherEvents.RecommendationSystemStrID | Array(String) | Строковый идентификатор источника трафика для статьи — рекомендательная система |
| PublisherEvents.MessengerStrID | Array(String) | Строковый идентификатор источника трафика для статьи — мессенджер |
| PublisherEvents.TurboTypeStr | Array(String) | Строковый идентификатор типа Турбо |
| TrafficSource.ModelStr | Array(String) | Строковый идентификатор типа атрибуции |
| TrafficSource.StrID | Array(String) | Строковый идентификатор источника трафика |
| TrafficSource.SearchEngineStrID | Array(String) | Строковый идентификатор поисковой системы (детально) |
| TrafficSource.SearchEngineRootID | Array(UInt16) | Идентификатор поисковой системы |
| TrafficSource.SearchEngineRootStrID | Array(String) | Строковый идентификатор поисковой системы |
| TrafficSource.AdvEnginePlaceID | Array(UInt64) | Идентификатор рекламной системы |
| TrafficSource.AdvEnginePlaceStrID | Array(String) | Строковый идентификатор рекламной системе |
| TrafficSource.SocialSourceNetworkStrID | Array(String) | Строковый идентификатор социальной сети, из которой был переход |
| TrafficSource.RecommendationSystemStrID | Array(String) | Строковый идентификатор рекомендательной системы |
| TrafficSource.MessengerStrID | Array(String) | Строковый идентификатор мессенджера |
| TrafficSource.QRCodeProviderID | Array(UInt16) | Провайдер QR-кодов |
| TrafficSource.QRCodeProviderStrID | Array(String) | Строковый идентификатор провайдера QR-кодов |
| TrafficSource.YQRID | Array(String) | Уникальная метка, которую проставляет Яндекс QR-генератор |
| UserIDHash | UInt64 | Идентификатор посетителя, сквозной в рамках одного счетчика, даже если он установлен на разных доменах |
| isRobotPro | UInt8 | Роботность визита по данным антифрода Директа и поведению на сайте. Возможные значения: 0 — не роботный визит; 1 — роботный визит. Примечание Данные в поле актуальны с 19 апреля 2025 года и доступны только на счетчиках в Метрике Про. |

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
