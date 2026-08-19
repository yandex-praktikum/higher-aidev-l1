> Источник: https://yandex.ru/support/metrica/ru/code/install-counter-fb
# Установка и настройка счетчика в Facebook Instant Articles

- [Установка счетчика](ru/code/install-counter-fb#integration)
- [Отправка параметров визитов](ru/code/install-counter-fb#params)
- [Отправка параметров посетителей](ru/code/install-counter-fb#user-params)
- [Пример интеграции счетчика](ru/code/install-counter-fb#example)[Узнайте больше](ru/code/install-counter-fb#uznajte-bolshe)

Счетчик Яндекс Метрики можно установить в [моментальные статьи Facebook](https://developers.facebook.com/docs/instant-articles)*** (Facebook Instant Articles).

Из-за особенностей реализации моментальных статей JavaScript-код счетчика изолирован от других HTML-элементов. Поэтому следующие возможности Метрики будут недоступны:

- Вебвизор;
- Карты кликов, ссылок и скроллинга;
- Аналитика форм;
- отправка данных электронной коммерции.

Чтобы добавить код Метрики в моментальную статью, нужно использовать специальные HTML-элементы.

## ru/code/install-counter-fb#integrationУстановка счетчика

Внимание

C моментальных статей Facebook*** (Facebook Instant Articles) невозможно собирать данные контентной аналитики.

Добавьте следующий код в элемент `body` моментальной статьи:

```
...
<figure class="op-tracker">
  <iframe>
    <!-- Код счетчика -->
  </iframe>
</figure>
...
```

Счетчик будет учитывать посещения для страницы, которая указана в элементе `head` как каноническая:

```
...
<head>
  <meta charset="utf-8">
  <link rel="canonical" href="http://example.com/page.html">
  <meta property="op:markup_version" content="v1.0">
</head>
...
```

Чтобы проверить работоспособность счетчика, воспользуйтесь [эндпоинтом от Facebook](https://developers.facebook.com/docs/instant-articles/analytics?#analytics-services)***.

## ru/code/install-counter-fb#paramsОтправка параметров визитов

1. Создайте JavaScript-объект `yaParams`: ... var yaParams = { title: "Article title", referrer: "Article referrer" } ...
2. Передайте параметры при инициализации счетчика: ... ym(*XXXXXXXX*, 'init', {params: window.yaParams||{}}); ... Facebook*** предоставляет [определенный набор данных](https://developers.facebook.com/docs/instant-articles/analytics#analytics-services) о моментальных статьях, которые можно использовать в качестве параметров визитов. Данные можно взять из JavaScript-объекта `ia_document`.

## ru/code/install-counter-fb#user-paramsОтправка параметров посетителей

1. Отправьте данные о просмотре с помощью метода [`hit`](ru/objects/hit) после инициализации счетчика: ... ym(*XXXXXXXX*, 'init', { defer: true }); ym(*XXXXXXXX*, 'hit', ia_document.shareURL, { referer: ia_document.referrer, title: ia_document.title }); ...
2. Отправьте параметры посетителей с помощью вызова функции [`userParams`](ru/objects/user-params): ... ym(*XXXXXXXX*, 'userParams', { user_key: "user_value"}); ...

## ru/code/install-counter-fb#exampleПример интеграции счетчика

```
<body>
  ...
  <figure class="op-tracker">
    <iframe>
      <script type="text/javascript"><script>
        (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
        (window, document, 'script', 'https://mc.yandex.ru/metrika/tag.js?id=XXXXXXXX', 'ym')

            ym(XXXXXXXX, 'init', { 
                trackLinks:true,
                accurateTrackBounce:true,
                params: window.yaParams||{title: "no title"}
            });

      </script>
      <noscript><div><img src="https://mc.yandex.ru/watch/XXXXXXXX" style="position:absolute; left:-9999px;" alt=""/></div></noscript>
    </iframe>
  </figure>
  ...
</body>
```

`XXXXXXXX` — номер вашего счетчика.

### ru/code/install-counter-fb#uznajte-bolsheУзнайте больше

- [Передача событий](ru/data/visit-params-data)
- [Аналитика в моментальных статьях](https://developers.facebook.com/docs/instant-articles/reference/analytics)

* Сервис, запрещенный на территории РФ.

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

Сервис, запрещенный на территории РФ.

XXXXXXXX — номер вашего счетчика.

### Была ли статья полезна?
