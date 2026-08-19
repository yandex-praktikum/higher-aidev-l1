> Источник: https://yandex.ru/support/metrica/ru/integrated-goal/nethouse-goal
# Цели Nethouse

- [Как это работает](ru/integrated-goal/nethouse-goal#how-works)
- [Где посмотреть статистику](ru/integrated-goal/nethouse-goal#viewing-statistics)
- [Ограничения](ru/integrated-goal/nethouse-goal#restrictions)

Если ваш сайт создан в [Nethouse](https://nethouse.ru), Метрика может автоматически создавать цели для отслеживания некоторых событий на сайте. Например, заказ, покупку или отправку форм обратной связи.

## ru/integrated-goal/nethouse-goal#how-worksКак это работает

Чтобы Метрика начала собирать данные по целям Nethouse:

1. [Установите счетчик Метрики](https://nethouse.ru/about/instructions/kak_ustanovit_schetchik_yandeks_metrika) на вашем сайте.
2. В настройках счетчика включите опцию **Автоматические цели**.

Дополнительные настройки Метрики или конструктора не требуются.

Цели для Nethouse автоматически создаются для отслеживания событий, перечисленных в таблице.

| Название цели в интерфейсе | Идентификатор события |
| --- | --- |
| Подписка на рассылку | ym-subscription-confirm |
| Форма Узнать о поступлении | ym-new-income-form-confirm |
| Товар заказан | ym-order-form-product-confirm |
| Услуга заказана | ym-order-form-service-confirm |
| Заказ в 1 клик | ym-one-click-form-confirm |
| Форма Написать нам | ym-feedback-form-confirm |
| Форма Обратный звонок | ym-callback-form-confirm |
| Отправка лид-формы | ym-lead-form-confirm |
| Просмотр корзины | ym-page-cart |
| Заказ оформлен | ym-page-checkout |
| Успешная оплата | ym-page-pay |

Вы можете управлять автоцелями Nethouse так же, как другими [автоматическими целями](ru/general/auto-goals): редактировать и удалять.

Если вам нужно отслеживать в Метрике другие события, их можно [добавить вручную](https://nethouse.ru/about/instructions/kak_ustanovit_schetchik_yandeks_metrika).

## ru/integrated-goal/nethouse-goal#viewing-statisticsГде посмотреть статистику

Чтобы посмотреть статистику по целям, воспользуйтесь отчетом [Конверсии](ru/reports/conversion): данные появятся в отчете, когда Метрика зафиксирует хотя бы одно событие. Также вы можете [добавлять](ru/reports/report-general#choose-goal) цели в другие отчеты Метрики для отслеживания поведения пользователей.

## ru/integrated-goal/nethouse-goal#restrictionsОграничения

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
