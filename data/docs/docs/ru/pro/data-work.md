> Источник: https://yandex.ru/support/metrica/ru/pro/data-work
# Как работать с данными

- [Скрипты для анализа последовательностей источников трафика](ru/pro/data-work#scripts)
- [Как правильно выгружать визиты](ru/pro/data-work#visits)
- [Как выгружать хиты](ru/pro/data-work#hits)
- [Как соотнести визит с его хитами](ru/pro/data-work#visit-hit)
- [Отчет «Посещаемость»](ru/pro/data-work#traffic)
- [Отчет «UTM метки»](ru/pro/data-work#utm)
- [Отчет «Популярное»](ru/pro/data-work#popular)
- [Отчет «Конверсия цели»](ru/pro/data-work#conversion)
- [Отчет «Источники, Сводка»](ru/pro/data-work#sources)
- [Отчет «Рекламные системы»](ru/pro/data-work#advertisement)
- [Отчет «Воронки ecommerce-событий» (нет в интерфейсе Метрики)](ru/pro/data-work#ecom-total)
- [Отчет «Воронки ecomerce-событий в различных срезах» (нет в интерфейсе Метрики)](ru/pro/data-work#ecom-slices)
- [Отчет «Удержание новых посетителей» (нет в интерфейсе Метрики)](ru/pro/data-work#retention)
- [Отчет «Удержание новых посетителей в различных срезах» (нет в интерфейсе Метрики)](ru/pro/data-work#retention-slices)

Примечание

Функция доступна только для пакета Метрика Про.

Неагрегированные данные сервиса [Яндекс Метрика](https://metrika.yandex.ru/) можно получать в свой Clickhouse-кластер, который расположен на [Yandex Cloud](https://cloud.yandex.ru/).

Этот механизм интеграции обладает следующими отличиями от [LogsAPI](https://yandex.ru/dev/metrika/doc/api2/logs/intro.html):

- Интеграция содержит расширенный набор полей.
- В визитах, в отличие от LogsAPI, атрибуция лежит массивами. Все массивы `TrafficSource.XXX` скоррелированы между собой по типу аттрибуции. Поле `XXX` в нужной атрибуции `YYY`: `TrafficSource.XXX[indexOf(TrafficSource.Model, YYY)] as XXX`. [Как правильно выгружать визиты](ru/pro/data-work#visits)
- В Визитах `FirstPartyCookie` аналогичен `clientid` в LogsAPI.

Внимание

Интеграция не является обратно совместимой с Logs API по формату данных.

## ru/pro/data-work#scriptsСкрипты для анализа последовательностей источников трафика

Скрипты формируют цепочки переходов для каждого пользователя, что позволяет получить:

- отчет по ассоциированным конверсиям из всех источников;
- отчеты в разных моделях атрибуции, в том числе которых нет в интерфейсе Метрики, например, линейной.

На основе данной информации можно самостоятельно посчитать самые популярные последовательности источников трафика, которые предшествуют конверсии.

Скрипты выложены на [GitHub](https://github.com/zhdanchik/yandex_metrika_connector_cases).

## ru/pro/data-work#visitsКак правильно выгружать визиты

Примечание

Данные в визитах обновляются по мере поступления новой информации о них. В среднем 99 % визитов завершаются в течение 3 дней после их начала.

```
SELECT
    VisitID,
    CounterID,
    StartDate,
    CounterUserIDHash, -- внутренний UserID, с которым работает Метрика
    FirstPartyCookie, -- то же самое, что и ClientID в LogsAPI
    Duration,
    EAction.Type,
    EndURL,
    Goals.ID,
    IsBounce,
    IsMobile,
    OS,
    OSFamily,
    OSName,
    PageViews,
    Referer,
    RegionID,
    StartURL,
    TrafficSource.ID, -- Значения в полях TrafficSource.ID означают: 
{-1: внутренние переходы; 0: прямые заходы; 
1: переходы по ссылкам на сайтах; 2: переходы из поисковых систем;
3: переходы по объявлениям; 4: переходы с сохраненных страниц;
5: Не определен; 6: Переходы по внешним ссылкам; 7: переходы с почтовых рассылок;
8: переходы из соц сетей; 9: переходы из рекомендательных систем; 
10: переходы из мессенджеров; 11: переходы по QR коду}
    TrafficSource.StrID, -- человеческое название источника трафика
    TrafficSource.Model, -- все массивы TrafficSource.XXX скоррелированы между собой.
Порядок элементов в них отражает по какой атрибуции TrafficSource.Model считается значение поля TraficSource.XXX, а внутри массива лежит само значение TraficSource.XXX
    TrafficSource.ID[indexOf(TrafficSource.Model, 1)] as last_TraficSourceID, -- Источник трафика по атрибуции Последний переход
    TrafficSource.ID[indexOf(TrafficSource.Model, 2)] as last_significant_TraficSourceID, -- Источник трафика по атрибуции Последний значимый переход
    TrafficSource.ID[indexOf(TrafficSource.Model, 3)] as first_TraficSourceID, -- Источник трафика по атрибуции Первый переход
    TrafficSource.ID[indexOf(TrafficSource.Model, 4)] as last_yandex_direct_TraficSourceID, -- Источник трафика по атрибуции Последний значимый переход Директ
    TrafficSource.ID[indexOf(TrafficSource.Model, 5)] as cd_last_significant_TraficSourceID, -- Источник трафика по атрибуции Последний значимый переход (кросс-девайс)
    TrafficSource.ID[indexOf(TrafficSource.Model, 6)] as cd_first_TraficSourceID, -- Источник трафика по атрибуции Первый переход (кросс-девайс)
    TrafficSource.ID[indexOf(TrafficSource.Model, 7)] as cd_last_yandex_direct_TraficSourceID, -- Источник трафика по атрибуции Последний значимый переход Директ (кросс-девайс)
    
    -- Если источник трафик реклама или продвижение, то можно посмотреть, какая это рекламная система. 
На примере последнего значимого источника трафика:
    If(last_significant_TraficSourceID = 3, TrafficSource.AdvEnginePlaceStrID[indexOf(TrafficSource.Model, 2)], 'not_ad') as last_significant_adv_engine_id,
    -- Если источник трафик поиск, то можно посмотреть, какая это поисковая система. 
На примере последнего значимого источника трафика:
    If(last_significant_TraficSourceID = 2, TrafficSource.SearchEngineStrID[indexOf(TrafficSource.Model, 2)], 'not_search') as last_significant_search_engine_id,
    -- Аналогично для остальных источников трафика: соц сети, рекомендательная система и т.д.
    UserAgent,
    WatchIDs -- для связки с WatchID из hits_all. В эту колонку не попадут хиты IsParameter = 1. В случае переполнения 500 хитов в этом массиве, остальные вывалятся за борт
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE StartDate = today() - 1 --сюда вставить любую дату, например, StartDate = toDate('2022-02-01') или StartDate = '2022-02-01'
    AND CounterID = toUInt32(24226447)
GROUP BY
    VisitID,
    CounterID,
    StartDate,
    CounterUserIDHash,
    FirstPartyCookie,
    Duration,
    EAction.Type,
    EndURL,
    Goals.ID,
    IsBounce,
    IsMobile,
    OS,
    OSFamily,
    OSName,
    PageViews,
    Referer,
    RegionID,
    StartURL,
    TrafficSource.Model,
    TrafficSource.ID,
    TrafficSource.StrID,
    last_TraficSourceID,
    last_significant_TraficSourceID,
    first_TraficSourceID, 
    last_yandex_direct_TraficSourceID,
    cd_last_significant_TraficSourceID,
    cd_first_TraficSourceID,
    cd_last_yandex_direct_TraficSourceID,
    last_significant_adv_engine_id,
    last_significant_search_engine_id,
    UserAgent,
    WatchIDs
HAVING sum(Sign) = 1
limit 1000
```

- Визиты могут обновляться в прошлое, например, при привязывании оффлайн-конверсии.
- При включении интеграции у самых первых визитов `sum(Sign)` может оказаться неконсистентным.

**Что будет, если не использовать `sum(Sign)`**

В логах коннектора лежат несколлапсированные версии визитов (т.е. несколько версий одного визита). Если их не коллапсировать, то данные будут неконсистентыми и один и тот же визит (его старые версии) будет учитываться более 1 раза.

Это происходит, потому что при обновлении визита старая версия (`VisitVersion = 1`, `Sign = 1`) не удаляется. Вместо этого добавляется полностью идентичная старой версии строчка, с разницей лишь в знаке `Sign` (`VisitVersion = 1`, `Sign = -1`). Далее добавляется уже обновленная версия визита с положительным `Sign` (`VisitVersion = 2`, `Sign = 1`). Таким образом, сделав `group by` по интересующим полям, получаем правильное и корректное число визитов через `sum(Sign)` за счет «схлопывания» неактуальных версий (`Sign = 1` и `Sign = -1` превратится в ноль).

```
select VisitID, VisitVersion, Sign
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
where StartDate = today()-3 -- сюда можно вставить любую дату
    AND (CounterID = toUInt32(24226447)) -- сюда вставить свой номер счетчика
    and VisitID in (select VisitID
                    from yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
                    where StartDate = today()-3 -- сюда можно вставить любую дату
                    group by VisitID
                    having count(distinct VisitVersion) > 3 -- для наглядности берем визит с более чем тремя изменениями (можно взять любое количество)
                    order by VisitID desc
                    limit 1 -- для нагладности берем 1 визит, можно взять больше
                    ) 
order by VisitID, VisitVersion, Sign
```

```
select VisitID, sum(Sign) as visits
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
where StartDate = today()-3 -- сюда можно вставить любую дату
    AND (CounterID = toUInt32(24226447)) -- сюда вставить свой номер счетчика
    and VisitID = 1243431264677003301
group by VisitID
```

`final` обрабатывает таблицу таким образом, чтобы версии уже были сколлапсированы. Убирает неактуальные версии визитов сам. Работает гораздо дольше, чем при подсчете через группировку и `sum(Sign)`.

```
select VisitID, VisitVersion, Sign
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
where StartDate = today()-3 -- сюда можно вставить любую дату
    AND (CounterID = toUInt32(24226447))
    and VisitID = 1243431264677003301
order by VisitID, VisitVersion, Sign
```

## ru/pro/data-work#hitsКак выгружать хиты

[Что такое хит](ru/pro/price#hit)

Примечание

При работе с хитами также необходимо учитывать их версионирование. По аналогии с визитами, один хит (`WatchID`) может иметь несколько `HitVersion`, которые можно сколлапсировать при помощи поля `Sign`. Важно выгружать хиты по таким же принципам, как это было описано в разделе [Как правильно выгружать визиты](ru/pro/data-work#visits). Также допускается использование конструкции `final`.

```
select CounterID,
        EventDate,
        CounterUserIDHash, -- внутренний UserID, с которым работает Метрика
        FirstPartyCookie, -- то же самое, что и ClientID в LogsAPI
        UTCEventTime,
        WatchID,
        Referer,
        OriginalURL, -- URL, в отличие от OriginalURL, может быть обрезан
        URL,
        UTMSource,
        IsMobile,
        OS,
        OSFamily,
        OSName,
        FirstPartyCookie,
        IsArtifical,
        IsDownload,
        IsLink,
        IsNotBounce,
        IsPageView,
        IsParameter
from yandex_data_transfer_test.hits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу хитов
where EventDate = today()-1 -- сюда вставить любую дату
   and CounterID = 24226447 -- сюда вставить номер своего счетчика
group by CounterID,
        EventDate,
        CounterUserIDHash, -- внутренний UserID, с которым работает Метрика
        FirstPartyCookie, -- то же самое, что и ClientID в LogsAPI
        UTCEventTime,
        WatchID,
        Referer,
        OriginalURL, -- URL, в отличие от OriginalURL, может быть обрезан
        URL,
        UTMSource,
        IsMobile,
        OS,
        OSFamily,
        OSName,
        FirstPartyCookie,
        IsArtifical,
        IsDownload,
        IsLink,
        IsNotBounce,
        IsPageView,
        IsParameter
having sum(Sign) = 1
```

## ru/pro/data-work#visit-hitКак соотнести визит с его хитами

Для соотнесения `VisitID` с принадлежащими ему хитами (`WatchID`) может быть недостаточно колонки `WatchIDs`. Это связано с тем, что в поле `WatchID` отсутствуют хиты-параметры визитов. Вы можете самостоятельно собрать список хитов, которые входят в визит. Для этого нужна дата начала визита, дата окончания визита и идентификатор посетителя.

```
select VisitID, -- в этом select будут визиты с собранном массивом его хитов
        CounterUserIDHash,
        UTCStartTime,
        Duration,
        UTCEndTime,
        groupArray(WatchID) as `watchids.id`,
        groupArray(IsPageView) as `watchids.is_page_view`,
        groupArray(IsParameter) as `watchids.is_parameter`,
        groupArray(UTCEventTime) as `watchids.is_utc_event_time`
from ( -- в этом select будут визиты, размноженные по каждому хиту
select VisitID,
        a.CounterUserIDHash as CounterUserIDHash,
        UTCStartTime,
        Duration,
        UTCEndTime,
        WatchID,
        IsPageView,
        IsParameter,
        UTCEventTime
from 
(select -- берем визиты, юзера, дату начала и дату окончания визита. Визит может продолжать обновляться в прошлое!
    VisitID,
    CounterUserIDHash,
    UTCStartTime,
    Duration,
    toDateTime(UTCStartTime) + Duration as UTCEndTime
from yandex_data_transfer_test.visits_dttql4la13mb206q472r final
where StartDate = '2023-04-01'
) as a
left join
(select -- берем хиты, юзера, дату и время хита. Исторические данные по хитам могут изменяться.
    WatchID,
    CounterUserIDHash,
    IsPageView,
    IsParameter,
    UTCEventTime
from yandex_data_transfer_test.hits_dttql4la13mb206q472r final
where EventDate >= '2023-04-01' 
        and EventDate <= toDate('2023-04-01')+5
        ) as b
on a.CounterUserIDHash = b.CounterUserIDHash -- важно ориентироваться именно на данный идентификатор посетителя
where UTCEventTime >= UTCStartTime and -- хиты со временем не раньше, чем начало визита 
        UTCEventTime <= UTCEndTime -- хиты со временем не позже, чем конец визита 
order by CounterUserIDHash, UTCEventTime
)
group by VisitID,
        CounterUserIDHash,
        UTCStartTime,
        Duration,
        UTCEndTime
limit 100
```

## ru/pro/data-work#trafficОтчет «Посещаемость»

```
SELECT StartDate AS `ym:s:date`, 
        sum(Sign) AS `ym:s:visits` -- правильное коллапсирование нескольких версий визита в самую последнюю и актуальную, и подсчет количества визитов
from yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
as `default.visits_all` 
WHERE `ym:s:date` >= toDate('2023-01-31') -- исторические данные до момента создания коннектора в данной версии не поддерживаются
        and `ym:s:date` <= toDate('2023-02-06') -- данные за "сегодня" (и медленные обновления за более поздние дни, например, оффлайн конверсии) могут доезжать с опозданием относительно интерфейса
        and CounterID = 24226447 -- поменять на свой номер счетчика
GROUP BY `ym:s:date` 
WITH TOTALS  
HAVING `ym:s:visits` >= 0.0 
ORDER BY `ym:s:date` ASC 
limit 0,7
```

```
SELECT
    toDate(StartDate) AS `ym:s:datePeriodday`,
    sum(Sign) AS `ym:s:visits`,
    uniqExact(CounterUserIDHash) AS `ym:s:users`,
    sum(PageViews * Sign) AS `ym:s:pageviews`,
    uniqExactIf(CounterUserIDHash, (`TrafficSource.StartTime`[indexOf(`TrafficSource.Model`, 3)]) = (`TrafficSource.StartTime`[indexOf(`TrafficSource.Model`, 1)])) / uniqExact(CounterUserIDHash) * 100. AS `ym:s:percentNewVisitors`, -- атрибуция 3 - это атрибуция "Первое посещение", 1 - это "Последнее посещение"
    100. * (sum(IsBounce * Sign) / `ym:s:visits`) AS `ym:s:bounceRate`,
    `ym:s:pageviews` / `ym:s:visits` AS `ym:s:pageDepth`,
    sum(Duration * Sign) / `ym:s:visits` AS `ym:s:avgVisitDurationSeconds`
   -- метрики Роботность и Кросс-девайс посетители недоступны в коннекторе
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
AS `default.visits_all`
WHERE (StartDate >= toDate('2023-03-10'))  
        AND (StartDate <= toDate('2023-03-16')) 
        AND (CounterID = toUInt32(24226447)) -- поменять на свой номер счетчика
GROUP BY `ym:s:datePeriodday`
WITH TOTALS
HAVING (`ym:s:visits` > 0.) OR (`ym:s:users` > 0.) OR (`ym:s:pageviews` > 0.)
ORDER BY `ym:s:datePeriodday` DESC
LIMIT 0, 50
```

## ru/pro/data-work#utmОтчет «UTM метки»

```
SELECT
    `TrafficSource.UTMSource`[indexOf(`TrafficSource.Model`, 2)] AS `ym:s:lastSignUTMSource`,
    sum(Sign) AS `ym:s:visits`,
    least(uniqExact(CounterUserIDHash), `ym:s:visits`) AS `ym:s:users`,
    100. * (sum(IsBounce * Sign) / `ym:s:visits`) AS `ym:s:bounceRate`,
    sum(PageViews * Sign) / `ym:s:visits` AS `ym:s:pageDepth`,
    sum(Duration * Sign) / `ym:s:visits` AS `ym:s:avgVisitDurationSeconds`,
    sumArray(arrayMap(x → (if(isFinite(x), x, 0) * Sign), arrayMap(x_0 → toInt64(notEmpty(x_0)), `EPurchase.ID`))) AS `ym:s:ecommercePurchases`
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE (StartDate >= toDate('2023-03-10')) 
        AND (StartDate <= toDate('2023-03-16')) 
        AND (CounterID = 24226447) -- сюда вставить свой номер счетчика
        AND (`ym:s:lastSignUTMSource` != '')
GROUP BY `ym:s:lastSignUTMSource`
HAVING (`ym:s:visits` > 0.) OR (`ym:s:users` > 0.) OR (`ym:s:ecommercePurchases` > 0.)
ORDER BY
    `ym:s:visits` DESC,
    `ym:s:lastSignUTMSource` ASC
LIMIT 0, 50
```

## ru/pro/data-work#popularОтчет «Популярное»

```
SELECT
    URLHash(URL, toInt8(0)) AS `ym:pv:URLPathLevel1Hash`,
    anyHeavyIf(domain(URL), domain(URL) != '') AS `ym:pv:URLPathLevel1HashFavicon`,
    max(URLHierarchy(ifNull(URL, ''))[1]) AS `ym:pv:URLPathLevel1`,
    sum(Sign * W) AS `ym:pv:pageviews`,
    least(uniq(CounterUserIDHash), `ym:pv:pageviews`) AS `ym:pv:users`
FROM yandex_data_transfer_test.hits_dttql4la13mb206q472r AS `default.hits_all`
WHERE (EventDate >= toDate('2023-03-10')) 
        AND (EventDate <= toDate('2023-03-16')) 
        and CounterID = 24226447 -- сюда вставить номер своего счетчика
       and IsPageView
GROUP BY `ym:pv:URLPathLevel1Hash`
HAVING `ym:pv:pageviews` > 0.0 AND (`ym:pv:pageviews` > 0.0 OR `ym:pv:users` > 0.0)
    WITH TOTALS
ORDER BY
    `ym:pv:pageviews` DESC,
    `ym:pv:URLPathLevel1` ASC,
    `ym:pv:URLPathLevel1Hash` ASC
LIMIT 0, 50
```

## ru/pro/data-work#conversionОтчет «Конверсия цели»

```
WITH 1. AS W, 17069575 as my_goal_id -- поменять на номер своей цели
SELECT
    toDate(StartDate) AS `ym:s:datePeriodday`,
    100. * (sum(has(`Goals.ID`, my_goal_id) * (Sign * W)) / sum(Sign * W)) AS `ym:s:goal17069575conversionRate`,
    sum(arrayCount(x → (my_goal_id = x), `Goals.ID`) * (Sign * W)) AS `ym:s:goal17069575reaches`,
    sumIf(Sign * W, arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`)) AS `ym:s:goal17069575visits`,
    least(toFloat64(uniqIf(CounterUserIDHash, arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`))), `ym:s:goal17069575visits`) AS `ym:s:goal17069575users`,
    sumIf(PageViews * (Sign * W), arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`)) AS `ym:s:goal17069575pageviews`,
    (least(uniqIf(CounterUserIDHash, ((`TrafficSource.StartTime`[indexOf(`TrafficSource.Model`, 3)]) = (`TrafficSource.StartTime`[indexOf(`TrafficSource.Model`, 1)])) AND arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`)), uniqIf(CounterUserIDHash, arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`))) / uniqIf(CounterUserIDHash, arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`))) * 100. AS `ym:s:goal17069575percentNewVisitors`,
    100. * (sumIf(IsBounce * (Sign * W), arrayExists(x_0 → (x_0 = my_goal_id), `Goals.ID`)) / `ym:s:goal17069575visits`) AS `ym:s:goal17069575bounceRate`,
    `ym:s:goal17069575pageviews` / `ym:s:goal17069575visits` AS `ym:s:goal17069575pageDepth`,
    sumIf(Duration * (Sign * W), arrayExists(x_0 -> (x_0 = my_goal_id), `Goals.ID`)) / `ym:s:goal17069575visits` AS `ym:s:goal17069575avgVisitDurationSeconds`
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE (StartDate >= toDate('2023-02-18')) 
        AND (StartDate <= toDate('2023-03-17')) 
        AND (CounterID = 24226447) -- поменять на свой номер счетчика
GROUP BY `ym:s:datePeriodday`
HAVING (`ym:s:goal17069575reaches` > 0.) AND ((`ym:s:goal17069575reaches` > 0.) OR (`ym:s:goal17069575visits` > 0.) OR (`ym:s:goal17069575users` > 0.) OR (`ym:s:goal17069575pageviews` > 0.))
ORDER BY `ym:s:datePeriodday` DESC
LIMIT 0, 50
```

## ru/pro/data-work#sourcesОтчет «Источники, Сводка»

```
WITH 1. AS W
SELECT
    `TrafficSource.ID`[indexOf(`TrafficSource.Model`, 2)] AS `ym:s:lastSignTrafficSource`,
    sum(Sign * W) AS `ym:s:visits`,
    least(toFloat64(uniq(CounterUserIDHash)), `ym:s:visits`) AS `ym:s:users`,
    100. * (sum(IsBounce * (Sign * W)) / `ym:s:visits`) AS `ym:s:bounceRate`,
    sum(PageViews * (Sign * W)) / `ym:s:visits` AS `ym:s:pageDepth`,
    sum(Duration * (Sign * W)) / `ym:s:visits` AS `ym:s:avgVisitDurationSeconds`
from yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE (StartDate >= toDate('2023-03-10')) 
        AND (StartDate <= toDate('2023-03-16')) 
        AND (CounterID = 24226447) -- поменять на свой номер счетчика
GROUP BY `ym:s:lastSignTrafficSource`
    WITH TOTALS
HAVING (`ym:s:visits` > 0.) OR (`ym:s:users` > 0.)
ORDER BY
    `ym:s:visits` DESC,
    `ym:s:lastSignTrafficSource` ASC
LIMIT 0, 50
```

```
WITH 1. AS W
SELECT
    `TrafficSource.ID`[indexOf(`TrafficSource.Model`, 2)] AS `ym:s:lastSignTrafficSource`,
    `TrafficSource.StrID`[indexOf(`TrafficSource.Model`, 2)] AS `ym:s:lastSignTrafficSourceName`,
     
    if(
        ((`TrafficSource.Domain`[indexOf(`TrafficSource.Model`, 2)]) != '') AND 
            (`ym:s:lastSignTrafficSource` IN (-1, toInt8(1))), 
        `TrafficSource.Domain`[indexOf(`TrafficSource.Model`, 2)], 
        if(`ym:s:lastSignTrafficSource` = toInt8(2), 
            `TrafficSource.SearchEngineStrID`[indexOf(`TrafficSource.Model`, 2)], 
            if(`ym:s:lastSignTrafficSource` = toInt8(3), `TrafficSource.AdvEnginePlaceStrID`[indexOf(`TrafficSource.Model`, 2)], 
                if(`ym:s:lastSignTrafficSource` = toInt8(8), toString(`TrafficSource.SocialSourceNetworkStrID`[indexOf(`TrafficSource.Model`, 2)]), 
                  if(`ym:s:lastSignTrafficSource` = toInt8(9), toString(if((`TrafficSource.RecommendationSystemID`[indexOf(`TrafficSource.Model`, 2)]) = 0, '1', `TrafficSource.RecommendationSystemStrID`[indexOf(`TrafficSource.Model`, 2)])), 
                     if(`ym:s:lastSignTrafficSource` = toInt8(10), toString(if((`TrafficSource.MessengerID`[indexOf(`TrafficSource.Model`, 2)]) = 0, '1', `TrafficSource.MessengerStrID`[indexOf(`TrafficSource.Model`, 2)])), 
                         if(`ym:s:lastSignTrafficSource` = toInt8(11), toString(`TrafficSource.QRCodeProviderStrID`[indexOf(`TrafficSource.Model`, 2)]), 
                                ''
                             )
                       )
                     )
                   )
               )
          )
       ) AS `ym:s:lastSignSourceEngine`,
    anyHeavy(if(`ym:s:lastSignTrafficSource` IN (-1, toInt8(1)), concatAssumeInjective('http://', `TrafficSource.Domain`[indexOf(`TrafficSource.Model`, 2)]), '')) AS `ym:s:lastSignSourceEngineURL`,
    sum(Sign * W) AS `ym:s:visits`,
    least(toFloat64(uniqExact(CounterUserIDHash)), `ym:s:visits`) AS `ym:s:users`,
    100. * (sum(IsBounce * (Sign * W)) / `ym:s:visits`) AS `ym:s:bounceRate`,
    sum(PageViews * (Sign * W)) / `ym:s:visits` AS `ym:s:pageDepth`,
    sum(Duration * (Sign * W)) / `ym:s:visits` AS `ym:s:avgVisitDurationSeconds`
FROM yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE (StartDate >= toDate('2023-03-10')) 
        and (StartDate >= toDate('2023-03-16')) 
        AND (CounterID = 24226447) -- поменять на свой номер счетчика
GROUP BY
    `ym:s:lastSignTrafficSource`,
    `ym:s:lastSignTrafficSourceName`,
    `ym:s:lastSignSourceEngine`
    WITH TOTALS
HAVING (`ym:s:visits` > 0.) OR (`ym:s:users` > 0.)
ORDER BY
    `ym:s:visits` DESC,
    `ym:s:lastSignTrafficSource` ASC,
    `ym:s:lastSignSourceEngine` ASC
LIMIT 0, 50
```

## ru/pro/data-work#advertisementОтчет «Рекламные системы»

```
WITH 1. AS W
SELECT
    `TrafficSource.AdvEnginePlaceStrID`[indexOf(`TrafficSource.Model`, 2)] as `ym:s:lastSignAdvEngine`, -- Рекламная система по атрибуции "Последний значимый переход"
    sum(Sign * W) AS `ym:s:visits`,
    least(toFloat64(uniqExact(CounterUserIDHash)), `ym:s:visits`) AS `ym:s:users`,
    100. * (sum(IsBounce * (Sign * W)) / `ym:s:visits`) AS `ym:s:bounceRate`,
    sum(PageViews * (Sign * W)) / `ym:s:visits` AS `ym:s:pageDepth`,
    sum(Duration * (Sign * W)) / `ym:s:visits` AS `ym:s:avgVisitDurationSeconds`
from yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
WHERE (StartDate = toDate('2023-03-15')) 
        AND (CounterID = 24226447) -- поменять на свой номер счетчика
        AND (`ym:s:lastSignAdvEngine` != '') 
        AND ((`TrafficSource.ID`[indexOf(`TrafficSource.Model`, 2)]) = toInt8(3)) -- источник трафик "Реклама" по атрибуции "Последний значимый переход"
GROUP BY `ym:s:lastSignAdvEngine`
    WITH TOTALS
HAVING (`ym:s:visits` > 0.) OR (`ym:s:users` > 0.)
ORDER BY
    `ym:s:visits` DESC,
    `ym:s:lastSignAdvEngine` ASC
LIMIT 0, 50
```

## ru/pro/data-work#ecom-totalОтчет «Воронки ecommerce-событий» (нет в интерфейсе Метрики)

Интеграция позволяет построить более сложные отчеты, которых нет в Метрике. Например, построить воронку по ecommerce-событиям.

Для этого отчета рекомендуем соблюдать условия:

- Настроены события `detail`, `add`, `purchase` и их корректная передача.
- От 10 посетителей в каждом из срезов.
- Конверсия в первый шаг больше 1 %.
- Есть достаточно данных по срезам, если они используются. [Отчет по Воронкам ecom-событий в различных срезах](ru/pro/data-work#ecom-slices)

```
select counter_id,
        step0_users, -- общее число посетителей
        step1_users, -- посетители, посмотревшие товары
        step2_users, -- посетители, посмотревшие товары, затем добавившие их в корзину
        step3_users, -- посетители, посмотревшие товары, затем добавившие их в корзину,
 затем совершившие покупку
        round(step0_users/step0_users*100, 4) as perc_step0, -- % общее число посетителей
        round(step1_users/step0_users*100, 4) as perc_step1, -- % посетителей, посмотревших товары
        round(step2_users/step0_users*100, 4) as perc_step2, -- % посетителей, посмотревших товары, затем добавивших их в корзину
        round(step3_users/step0_users*100, 4) as perc_step3 -- % посетителей, посмотревших товары, затем добавивших их в корзину, затем совершивших покупку

from

(select 
        counter_id,
        sum(step_1) as step1_users,
        sum(step_2) as step2_users,
        sum(step_3) as step3_users
    from
        (select
            CounterID as counter_id,
            CounterUserIDHash as user_id,
            max(e.Type = 1) as step_1, -- только просмотр товаров
            sequenceMatch('(?1)(?2)')(e.EventTime, (e.Type = 1), (e.Type = 4)) as step_2, -- просмотр товаров, а затем добавление в корзину
            sequenceMatch('(?1)(?2)(?3)')(e.EventTime, (e.Type = 1), (e.Type = 4), (e.Type = 3)) as step_3 -- просмотр товаров, затем добавление в корзину, затем покупка
        from 
            (select 
                CounterUserIDHash,
                CounterID,
                e.Type, -- типы еком событий (1 - detail, 2 - стейт корзины, 3 - покупка, 4 - добавление в корзину, 5 - удаление из корзины)
                e.EventTime
            from yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
            array join EAction as e --arrayJoin размножает массив с еком-событиями в отдельные строки
            where (StartDate >= '2023-02-01')
                and (StartDate <= '2023-02-28')
                and CounterID = 24226447 -- поменять на свой номер счетчика
                ) 
        group by counter_id, user_id
        )
    group by counter_id) as a

inner join (select
        CounterID as counter_id,
        uniqExact(CounterUserIDHash) as step0_users 
    from yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
    where (StartDate >= '2023-02-01') 
        and (StartDate <= '2023-02-28')
        and CounterID = 24226447 -- поменять на свой номер счетчика
    group by counter_id) as b
on a.counter_id = b.counter_id
```

## ru/pro/data-work#ecom-slicesОтчет «Воронки ecomerce-событий в различных срезах» (нет в интерфейсе Метрики)

Также можно построить воронку по различным срезам: источник трафика, операционная система, устройство.

```
select counter_id,
        is_mobile,
        step0_users, -- общее число посетителей
        step1_users, -- посетители, посмотревшие товары
        step2_users, -- посетители, посмотревшие товары, затем добавившие их в корзину
        step3_users, -- посетители, посмотревшие товары, затем добавившие их в корзину, затем совершившие покупку
        round(step0_users/step0_users*100, 4) as perc_step0, -- % общее число посетителей
        round(step1_users/step0_users*100, 4) as perc_step1, -- % посетителей, посмотревших товары
        round(step2_users/step0_users*100, 4) as perc_step2, -- % посетителей, посмотревших товары, затем добавивших их в корзину
        round(step3_users/step0_users*100, 4) as perc_step3 -- % посетителей, посмотревших товары, затем добавивших их в корзину, затем совершивших покупку

from

(select 
        counter_id,
        is_mobile,
        sum(step_1) as step1_users,
        sum(step_2) as step2_users,
        sum(step_3) as step3_users
    from
        (select
            CounterID as counter_id,
            CounterUserIDHash as user_id,
            is_mobile,
            max(e.Type = 1) as step_1, -- только просмотр товаров
            sequenceMatch('(?1)(?2)')(e.EventTime, (e.Type = 1), (e.Type = 4)) as step_2, -- просмотр товаров, а затем добавление в корзину
            sequenceMatch('(?1)(?2)(?3)')(e.EventTime, (e.Type = 1), (e.Type = 4), (e.Type = 3)) as step_3 -- просмотр товаров, затем добавление в корзину, затем покупка
        from 
            (select 
                CounterUserIDHash,
                CounterID,
                IsMobile as is_mobile,
                e.Type, -- типы еком событий (1 - detail, 2 - стейт корзины, 3 - покупка, 4 - добавление в корзину, 5 - удаление из корзины)
                e.EventTime
            from yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
            array join EAction as e --arrayJoin размножает массив с еком-событиями в отдельные строки
            where (StartDate >= '2023-02-01')
                and (StartDate <= '2023-02-28')
                and CounterID = 24226447 -- поменять на свой номер счетчика
                ) 
        group by counter_id, user_id, is_mobile
        )
    group by counter_id, is_mobile) as a

inner join (select
        CounterID as counter_id,
        IsMobile as is_mobile,
        uniqExact(CounterUserIDHash) as step0_users 
    from yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
    where (StartDate >= '2023-02-01') 
        and (StartDate <= '2023-02-28')
        and CounterID = 24226447 -- поменять на свой номер счетчика
    group by counter_id, is_mobile) as b
on a.counter_id = b.counter_id and a.is_mobile = b.is_mobile
```

## ru/pro/data-work#retentionОтчет «Удержание новых посетителей» (нет в интерфейсе Метрики)

```
with main as 

(select 
        counter_id,
        num_week,
        uniq(user_id) as users
from
    (select 
        CounterUserIDHash as user_id,
        CounterID as counter_id,
        toDate(FirstVisit) as first_date, -- первый визит посетителя на сайте
        StartDate as event_date,
        (toMonday(event_date) - toMonday(first_date))/7 as num_week
    from yandex_data_transfer_test.visits_dttql4la13mb206q472r final -- сюда вставить свою базу и свою таблицу визитов
    where event_date >= '2022-12-01' -- окно в 15 недель
        and event_date <= toDate('2022-12-31') + 92 -- окно в 15 недель
        and first_date >= '2022-12-01' -- берем только новых посетителей, которые пришли в декабре
        and first_date <= '2022-12-31' -- берем только новых посетителей, которые пришли в декабре
        and counter_id = 24226447 -- поменять на свой номер счетчика
    )
group by 
    counter_id,
    num_week
order by num_week)

select counter_id, 
        a.users as users, 
        b.users as users_first_week,
        round(a.users/b.users*100, 4) as perc_retention
from main as a
inner join (select * from main where num_week = 0) as b
on a.counter_id = b.counter_id
```

## ru/pro/data-work#retention-slicesОтчет «Удержание новых посетителей в различных срезах» (нет в интерфейсе Метрики)

Также можно добавить срез и сравнивать удержание в разных срезах. Мы рекомендуем, чтобы в срезе было хотя бы 30 посетителей, а сам срез составлял хотя бы 5% от общего числа.

```
with main as 

(select 
        counter_id,
        param,
        num_week,
        uniq(user_id) as users
from
    (select 
        CounterUserIDHash as user_id,
        CounterID as counter_id,
        toDate(FirstVisit) as first_date, -- первый визит посетителя на сайте
        StartDate as event_date,
        (toMonday(event_date) - toMonday(first_date))/7 as num_week,
        TrafficSource.ID[indexOf(TrafficSource.Model, 3)] as param
    from yandex_data_transfer_test.visits_dttql4la13mb206q472r -- сюда вставить свою базу и свою таблицу визитов
    where event_date >= '2022-12-01' -- окно в 15 недель
        and event_date <= toDate('2022-12-31') + 92 -- окно в 15 недель
        and first_date >= '2022-12-01' -- берем только новых посетителей, 
которые пришли в декабре
        and first_date <= '2022-12-31' -- берем только новых посетителей, 
которые пришли в декабре
        and counter_id = 24226447 -- поменять на свой номер счетчика
    )
group by 
    counter_id,
    param,
    num_week,
    param
order by param, num_week)

select counter_id, 
        param,
        a.users as users, 
        b.users as users_first_week,
        round(a.users/b.users*100, 4) as perc_retention
from main as a
inner join (select * from main where num_week = 0) as b
on a.counter_id = b.counter_id and a.param = b.param
```

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
