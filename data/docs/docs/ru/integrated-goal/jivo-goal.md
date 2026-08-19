> Источник: https://yandex.ru/support/metrica/ru/integrated-goal/jivo-goal
# Цели Jivo

- [Как это работает](ru/integrated-goal/jivo-goal#how-works)
- [Где посмотреть статистику](ru/integrated-goal/jivo-goal#viewing-statistics)
- [Ограничения](ru/integrated-goal/jivo-goal#restrictions)

Если вы используете чат [Jivo](https://www.jivo.ru/) на своем сайте, то с помощью автоматических целей можете отслеживать и анализировать статистику по действиям с чатом в отчетах Метрики.

## ru/integrated-goal/jivo-goal#how-worksКак это работает

Чтобы Метрика начала собирать данные по автоцелям Jivo, в настройках счетчика должна быть включена опция **Автоматические цели**.

Дополнительные настройки Метрики или чата не требуются. Jivo сам определит наличие счетчика и его номер на вашем сайте и передаст ему событие.

[Информация о сборе статистики](https://www.jivo.ru/help/integrations/otslezhyvanye-sobytyi-y-konversyi-jivosite-v-google-analytics-y-yandeks-metryke.html)

Цели для чата Jivo автоматически создаются для отслеживания событий, перечисленных в таблице.

| Название цели в интерфейсе | Идентификатор события | Описание события |
| --- | --- | --- |
| Автоцель Jivo: запуск чата клиентом | Jivo_Client_initiate_chat | Чат начат со стороны клиента. Возникает при отправке клиентом сообщения в форму чата при условии, что активное приглашение ранее не было показано |
| Автоцель Jivo: автоприглашение в чат | Jivo_Proactive_invitation_accepted | Клиент принял активное приглашение, написав сообщение в ответ. Также срабатывает при нажатии кнопки чата в мобильной версии, если до этого сработало активное приглашение |
| Автоцель Jivo: ручное приглашение в чат | Jivo_Client_answer_on_agent_request | Оператор вручную начал диалог с клиентом через функцию Посетители , а посетитель ответил, отправив сообщение в чат |
| Автоцель Jivo: офлайн-сообщение | Jivo_Offline_message_sent | Клиент отправил офлайн-сообщение |

Вы можете управлять автоцелями Jivo так же, как другими [автоматическими целями](ru/general/auto-goals): редактировать и удалять.

Если вам нужно отслеживать в Метрике другие события Jivo, их можно [добавить вручную](https://www.jivo.ru/help/integrations/otslezhyvanye-sobytyi-y-konversyi-jivosite-v-google-analytics-y-yandeks-metryke.html#yandex-metrika).

## ru/integrated-goal/jivo-goal#viewing-statisticsГде посмотреть статистику

Чтобы посмотреть статистику по целям, воспользуйтесь отчетом [Конверсии](ru/reports/conversion): данные появятся в отчете, когда Метрика зафиксирует хотя бы одно событие. Также вы можете [добавлять](ru/reports/report-general#choose-goal) цели в другие отчеты Метрики для отслеживания поведения пользователей.

## ru/integrated-goal/jivo-goal#restrictionsОграничения

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
