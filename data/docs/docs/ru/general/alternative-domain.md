> Источник: https://yandex.ru/support/metrica/ru/general/alternative-domain
# Загрузка счетчика с альтернативного домена

Обычно счетчик загружается с домена `mc.yandex.ru`. Чтобы загружать счетчик с домена `mc.yandex.com`, замените URL библиотеки в коде счетчика:

```
<!-- Yandex Metrica tag -->
...
   (window, document, "script", "https://mc.yandex.com/metrika/tag.js", "ym");
...
<noscript><div><img src="https://mc.yandex.com/watch/..." style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
```

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
