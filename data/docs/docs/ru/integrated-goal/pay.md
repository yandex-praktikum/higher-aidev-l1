> Источник: https://yandex.ru/support/metrica/ru/integrated-goal/pay
# Цель Яндекс Пэй

- [Как это работает](ru/integrated-goal/pay#how-works)
- [Где посмотреть статистику](ru/integrated-goal/pay#viewing-statistics)
- [Ограничения](ru/integrated-goal/pay#restrictions)

Если вы используете [Яндекс Пэй](https://bank.yandex.ru/pay), то с помощью автоматической цели можете отслеживать переход клиента в оплату через этот сервис в отчетах Метрики.

## ru/integrated-goal/pay#how-worksКак это работает

Чтобы Метрика начала собирать данные по автоцели Яндекс Пэй:

1. [Установите счетчик Метрики](ru/general/creating-counter) на вашем сайте.
2. В настройках счетчика включите опцию **Автоматические цели**.

Дополнительные настройки Метрики или Яндекс Пэй не требуются. Сервис Яндекс Пэй сам определит наличие счетчика и его номер на вашем сайте и передаст ему событие.

Цель для Яндекс Пэй автоматически создается для отслеживания события:

| Название цели в интерфейсе | Идентификатор события | Описание события |
| --- | --- | --- |
| Переход в оплату Яндекс Пэй | ym-begin-yapay | Клиент перешел в оплату через Яндекс Пэй |

Вы можете управлять автоцелями Яндекс Пэй так же, как другими [автоматическими целями](ru/general/auto-goals): редактировать и удалять.

## ru/integrated-goal/pay#viewing-statisticsГде посмотреть статистику

Чтобы посмотреть статистику по цели, воспользуйтесь отчетом [Конверсии](ru/reports/conversion): данные появятся в отчете, когда Метрика зафиксирует хотя бы одно событие. Также вы можете [добавлять](ru/reports/report-general#choose-goal) цель в другие отчеты Метрики для отслеживания поведения пользователей.

## ru/integrated-goal/pay#restrictionsОграничения

- Автоматические цели не учитываются в общем количестве целей счетчика.
- Автоматическая цель не будет создана, если на счетчике уже есть цель с точно таким же условием.
- source: ru/_includes/general/goal-page-visit/id-general/6.md Данный тип цели невозможно использовать в [Составной цели](ru/general/goal-steps). endsource: ru/_includes/general/goal-page-visit/id-general/6.md
- source: ru/_includes/general/goal-page-visit/id-general/2.md Сервис фиксирует достижение посетителем одной и той же цели на одном счетчике не чаще, чем раз в секунду. endsource: ru/_includes/general/goal-page-visit/id-general/2.md
- source: ru/_includes/general/goal-page-visit/id-general/3.md Во время одного визита посетителя сервис может фиксировать до 1000 достижений офлайн-целей и 400 достижений онлайн-целей, созданных для счетчика. endsource: ru/_includes/general/goal-page-visit/id-general/3.md
- source: ru/_includes/general/goal-page-visit/id-general/4.md При редактировании счетчика или цели накопленная ранее информация не изменяется. endsource: ru/_includes/general/goal-page-visit/id-general/4.md
- source: ru/_includes/general/goal-page-visit/id-general/5.md Если вы удалите цель, собранная по ней информация будет недоступна в отчетах. endsource: ru/_includes/general/goal-page-visit/id-general/5.md

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
