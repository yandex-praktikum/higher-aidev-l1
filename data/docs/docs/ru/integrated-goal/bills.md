> Источник: https://yandex.ru/support/metrica/ru/integrated-goal/bills
# Цели Яндекс Билетов

- [Как это работает](ru/integrated-goal/bills#how-works)
- [Где посмотреть статистику](ru/integrated-goal/bills#viewing-statistics)
- [Ограничения](ru/integrated-goal/bills#jivo-limits)

Если на вашем сайте установлен [виджет Яндекс Билеты](https://yandex.ru/support/tickets/widget/generate-widget.html), то с помощью автоматических целей можете отслеживать и анализировать статистику по поиску, выбору, бронированию и покупке билетов на сайте в отчетах Метрики.

## ru/integrated-goal/bills#how-worksКак это работает

Чтобы Метрика начала собирать данные по автоцелям Яндекс Билетов:

1. [Установите счетчик Метрики](ru/general/creating-counter) на вашем сайте.
2. В настройках счетчика включите опцию **Автоматические цели**.
3. Отправьте номер счетчика в службу поддержки Яндекс Билетов через [форму обратной связи](https://forms.yandex.ru/surveys/10029405.48af1e113375fefe3fb5fe3ccb7d88f430d8a221/).

Как только Метрика зафиксирует отправку данных, автоцели появятся. Дополнительные настройки Метрики или Билетов не требуются. Цели для Яндекс Билетов автоматически создаются для отслеживания событий, перечисленных в таблице.

[Информация о сборе статистики](https://yandex.ru/support/tickets/ru/widget/metrics.html#ya-metric)

| Название цели в интерфейсе | Идентификатор события | Описание события |
| --- | --- | --- |
| Автоцель Яндекс Билеты: открытие виджета | yndx-afisha-wg-goals-tickets-widget_open | Открытие любого виджета Яндекс Билетов |
| Автоцель Яндекс Билеты: выбор мест или билетов | yndx-afisha-wg-goals-tickets-widget_session | Открытие схемы зала или списка билетов |
| Автоцель Яндекс Билеты: ввод персональных данных | yndx-afisha-wg-goals-tickets-widget_personaldata | Пользователь вводит свои данные при оформлении заказа |
| Автоцель Яндекс Билеты: подтверждение заказа | yndx-afisha-wg-goals-tickets-widget_confirm | Посетитель выбрал способ оплаты и переходит к покупке |
| Автоцель Яндекс Билеты: оплата заказа | yndx-afisha-wg-goals-tickets-widget_payment | Заполнение формы оплаты |
| Автоцель Яндекс Билеты: покупка | yndx-afisha-wg-goals-tickets-widget_order | Посетитель совершил успешную оплату на сайте |

Вы можете управлять автоцелями Яндекс Билеты так же, как другими [автоматическими целями](ru/general/auto-goals): редактировать и удалять.

Если вам нужно отслеживать в Метрике другие события Яндекс Билетов, их можно [добавить вручную](https://yandex.ru/support/tickets/widget/metrics.html#ya-metric).

## ru/integrated-goal/bills#viewing-statisticsГде посмотреть статистику

Чтобы посмотреть статистику по целям, воспользуйтесь отчетом [Конверсии](ru/reports/conversion): данные появятся в отчете, когда Метрика зафиксирует хотя бы одно событие. Также вы можете [добавлять](ru/reports/report-general#choose-goal) цели в другие отчеты Метрики для отслеживания поведения пользователей.

## ru/integrated-goal/bills#jivo-limitsОграничения

- Автоматические цели не учитываются в общем количестве целей счетчика.
- source: ru/_includes/general/goal-page-visit/id-general/6.md Данный тип цели невозможно использовать в [Составной цели](ru/general/goal-steps). endsource: ru/_includes/general/goal-page-visit/id-general/6.md
- source: ru/_includes/general/goal-page-visit/id-general/2.md Сервис фиксирует достижение посетителем одной и той же цели на одном счетчике не чаще, чем раз в секунду. endsource: ru/_includes/general/goal-page-visit/id-general/2.md
- source: ru/_includes/general/goal-page-visit/id-general/3.md Во время одного визита посетителя сервис может фиксировать до 1000 достижений офлайн-целей и 400 достижений онлайн-целей, созданных для счетчика. endsource: ru/_includes/general/goal-page-visit/id-general/3.md
- source: ru/_includes/general/goal-page-visit/id-general/4.md При редактировании счетчика или цели накопленная ранее информация не изменяется. endsource: ru/_includes/general/goal-page-visit/id-general/4.md
- source: ru/_includes/general/goal-page-visit/id-general/5.md Если вы удалите цель, собранная по ней информация будет недоступна в отчетах. endsource: ru/_includes/general/goal-page-visit/id-general/5.md

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
