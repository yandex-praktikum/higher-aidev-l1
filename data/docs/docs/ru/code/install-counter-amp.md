> Источник: https://yandex.ru/support/metrica/ru/code/install-counter-amp
# Установка и настройка счетчика на сайт с AMP

- [Подключение счетчика на сайт с AMP](ru/code/install-counter-amp#how-to)
- [Передача данных](ru/code/install-counter-amp#data)[Отправка параметров визитов и посетителей](ru/code/install-counter-amp#params)[Точный показатель отказов](ru/code/install-counter-amp#bounce)[Достижение цели](ru/code/install-counter-amp#goal)[Скроллинг страницы](ru/code/install-counter-amp#scroll)[Скроллинг бесконечной ленты](ru/code/install-counter-amp#next-page-scroll)[Загрузка отдельного элемента страницы](ru/code/install-counter-amp#visible)[Общий пример кода счетчика](ru/code/install-counter-amp#general-amp)[Узнайте больше](ru/code/install-counter-amp#uznajte-bolshe)

Счетчик Яндекс Метрики предполагает выполнение JavaScript-кода. При установке кода счетчика на сайт, который использует технологию [Accelerated Mobile Pages](https://amp.dev/about/how-amp-works/) (AMP), страницы сайта не пройдут [валидацию](https://validator.ampproject.org/). Это объясняется тем, что технология AMP накладывает некоторые ограничения на использование возможностей JavaScript и HTML5. Поэтому можно установить счетчик специальным способом.

Примечание

При этом не поддерживается ряд функций Яндекс Метрики: [Электронная коммерция](ru/ecommerce/about), [Вебвизор](ru/webvisor/info), отслеживание нажатий [кнопки «Поделиться»](ru/content/share-button).

## ru/code/install-counter-amp#how-toПодключение счетчика на сайт с AMP

Внимание

C сайтов, которые используют технологию Accelerated Mobile Pages (AMP), невозможно собирать данные контентной аналитики.

Внесите изменения в HTML-код страниц вашего сайта:

1. Для отслеживания действий посетителей на страницах сайта с AMP используется дополнительный компонент [amp-analytics](https://amp.dev/documentation/components/amp-analytics/?format=websites). Добавьте его в код страниц вашего сайта — внутрь элемента `head`: <head> ... <script async custom-element="amp-analytics" src="https://cdn.ampproject.org/v0/amp-analytics-0.1.js"></script> ... </head>
2. Внесите изменения в элемент `body`: добавьте элемент `amp-analytics`. Чтобы данные о посещениях передавались в Метрику, укажите для атрибута `type` значение `metrika`, а также номер счетчика с помощью переменной `counterId`. <body> ... <amp-analytics type="metrika"> <script type="application/json"> { "vars": { "counterId": "XXXXXXXX" ... } } </script> </amp-analytics> ... </body>

## ru/code/install-counter-amp#dataПередача данных

Внимание

Когда пользователь открывает AMP-страницу, Яндекс Метрика фиксирует *просмотр* (`pageview`). Поэтому вам не нужно дополнительно передавать это событие. Если вы отправите его, в отчетах Яндекс Метрики будет отображаться неверное количество просмотров.

Для передачи данных при инициализации счетчика используются:

- переменная [yaParams](ru/data/visit-params-data) — для отправки параметров визитов;
- атрибуты [триггеров](https://amp.dev/documentation/components/amp-analytics/?format=websites#triggers) — для передачи событий (например, достижения цели).

### ru/code/install-counter-amp#paramsОтправка параметров визитов и посетителей

Пример передачи произвольных [параметров визита](ru/data/visit-params-data) и [параметров посетителей](ru/data/user-params-data) в момент посещения сайта с помощью переменной yaParams:

```
...
"vars": {
             "counterId": "XXXXXXXX",
             "yaParams": "{\"key\":\"value\",\"__ymu\":{\"user_param_key\":\"user_param_value\"}}"
},
...
```

Также можно передать только параметры визита или только параметры посетителя:

```
...
"vars": {
             "counterId": "XXXXXXXX",
             "yaParams": "{\"key\":\"value\"}"
},
...
```

```
...
"vars": {
             "counterId": "XXXXXXXX",
             "yaParams": "{\"__ymu\":{\"user_param_key\":\"user_param_value\"}}"
},
...
```

### ru/code/install-counter-amp#bounceТочный показатель отказов

Чтобы зафиксировать точный показатель отказа, используйте атрибут триггера [timer](https://amp.dev/documentation/components/amp-analytics/?format=websites#timer-trigger):

```
{
    ...
    "triggers": {
        "notBounce": {
            "on": "timer",
            "timerSpec": {
                "immediate": false,
                "interval": 15,
                "maxTimerLength": 14
            },
            "request": "notBounce"
        },
        ...
    }
}
```

### ru/code/install-counter-amp#goalДостижение цели

Чтобы отслеживать достижение цели при клике на определенный элемент страницы, используйте атрибут триггера [click](https://amp.dev/documentation/components/amp-analytics/?format=websites#click-trigger).

```
{
    ...
    "triggers": {
        "someGoalReach": {
            "on": "click",
            "selector": "#Button",
            "request": "reachGoal",
            "vars": {
                "goalId": "superGoalId",
                "yaParams": "{\"key\": \"value\"}" // В качестве параметров визита при достижении цели будет использоваться значение переменной из события
            }
        },
        ...
    }
}
```

| Поле | Тип | Описание |
| --- | --- | --- |
| goalId | String | Идентификатор цели, который задается при создании цели типа JavaScript-событие в интерфейсе Метрики |

### ru/code/install-counter-amp#scrollСкроллинг страницы

Вы можете фиксировать скроллинг страницы до определенной точки (долю в процентах от всей высоты страницы) с помощью атрибута тригерра [scroll](https://amp.dev/documentation/components/amp-analytics/?format=websites#scroll-trigger). Это событие может быть задано в качестве цели.

```
{
    ...
    "triggers": {
        "halfScroll": {
            "on": "scroll",
            "scrollSpec": {
                "verticalBoundaries": [
                    50
                ]
            },
            "request": "reachGoal",
            "vars": {
                "goalId": "halfScrollGoal"
             }
        },
        "partsScroll": {
            "on": "scroll",
            "scrollSpec": {
                "verticalBoundaries": [
                    25,
                    90
                ]
            },
            "request": "reachGoal",
            "vars": {
                    "goalId": "partsScrollGoal"
            }
        },
        ...
    }
}
```

### ru/code/install-counter-amp#next-page-scrollСкроллинг бесконечной ленты

Бесконечная лента может применяться для просмотра статей, следующих друг за другом. Чтобы фиксировать переходы от статьи к статье и просмотры каждой из них, используйте триггер [amp-next-page-scroll](https://amp.dev/documentation/components/amp-next-page/#analytics).

```
{
    ...
    "triggers": {
        "trackScrollThrough": {
             "on": "amp-next-page-scroll",
             "request": "pageview"
        },
        ...
    }
}
```

### ru/code/install-counter-amp#visibleЗагрузка отдельного элемента страницы

Чтобы фиксировать момент отображения на экране элементов страницы, используйте атрибут триггера [visible](https://amp.dev/documentation/components/amp-analytics/?format=websites#page-and-element-visibility-trigger).

### ru/code/install-counter-amp#general-ampОбщий пример кода счетчика

Пример кода приведен только для иллюстрации возможностей счетчика. При его копировании удалите комментарии (//<...>), вместо XXXXXXXX укажите номер вашего счетчика, а также внесите дополнительные изменения (например, настройте передачу параметров посетителей и визитов).

```
<body>
    ...
        <amp-analytics type="metrika">
            <script type="application/json">
                {
                    // Отправка параметров визита и посетителя
                    "vars": {
                        "counterId": "XXXXXXXX",
                        "yaParams": "{\"key\":\"value\",\"__ymu\":{\"user_param_key\":\"user_param_value\"}}"
                    },
                    // Передача триггеров
                    "triggers": {
                        // Точный показатель отказов
                        "notBounce": {
                            "on": "timer",
                            "timerSpec": {
                                "immediate": false,
                                "interval": 15,
                                "maxTimerLength": 14
                            },
                            "request": "notBounce"
                        },
                        // Скроллинг страницы
                        "halfScroll": {
                            "on": "scroll",
                            "scrollSpec": {
                                "verticalBoundaries": [
                                    50
                                ]
                            },
                            // Отслеживание скроллинга как цели
                            "request": "reachGoal",
                            "vars": {
                                "goalId": "halfScrollGoal"
                            }
                        },
                        // Скроллинг страницы
                        "partsScroll": {
                            "on": "scroll",
                            "scrollSpec": {
                                "verticalBoundaries": [
                                    25,
                                    90
                                ]
                            },
                            // Отслеживание скроллинга как цели 
                            "request": "reachGoal",
                            "vars": {
                                "goalId": "partsScrollGoal"
                            }
                        },
                        // Скроллинг бесконечной ленты
                        "trackScrollThrough": {
                            "on": "amp-next-page-scroll",
                            "request": "pageview"
                        }
                    }
                }
            </script>
        </amp-analytics>
    ...
</body>
```

### ru/code/install-counter-amp#uznajte-bolsheУзнайте больше

- [Общие указания по интеграции инструментов аналитики на сайт с AMP](https://github.com/ampproject/amphtml/blob/master/extensions/amp-analytics/integrating-analytics.md)

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Если вам не удалось [самостоятельно проверить работу счетчика](ru/general/check-counter), воспользуйтесь рекомендациями ниже.

Это может происходить по нескольким причинам:

- Счетчик установлен неправильно. Например, CMS внесла изменения в код счетчика. Следует переустановить счетчик или обратиться в службу поддержки вашей CMS.
- Работу счетчика Яндекс Метрики на сайте блокируют неработающие скрипты. Проверить это можно в консоли браузера.

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

Это значит, что информация отправляется Яндекс Метрике. При этом данные могут не отображаться в отчетах по следующим причинам:

- Данные отправляются на счетчик с другим номером.
- В настройках счетчика, на вкладке **Фильтры**, указаны слишком жесткие фильтры. Удалите ненужные фильтры.
- В настройках счетчика, на вкладке **Фильтры**, задан фильтр **Не учитывать мои визиты**. Это значит, что счетчик не учитывает ваши посещения — попробуйте перейти на сайт в режиме браузера «инкогнито».

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

Загрузка страницы сайта при переходе посетителя на нее. К просмотрам также относятся перезагрузка страницы, обновление AJAX-сайтов, отправка данных с помощью [метода hit](https://yandex.ru/support/metrica/objects/hit.html).

**Тип**

String

**Описание**

Идентификатор цели, который задается при создании цели типа [JavaScript-событие](https://yandex.ru/support/metrica/general/goal-js-event.html) в интерфейсе Метрики.

### Была ли статья полезна?
