> Источник: https://yandex.ru/support/metrica/ru/code/install-counter-csp
# Установка счетчика на сайт с CSP

- [Размещение кода счетчика в HTML-коде страниц сайта](ru/code/install-counter-csp#nonce)
- [Подключение кода счетчика с помощью внешнего скрипта](ru/code/install-counter-csp#separate-code-file)

Код счетчика, генерируемый Яндекс Метрикой, предназначен для размещения внутри HTML-кода страниц (inline). На сайтах, которые используют технологию [Content Security Policy](https://www.w3.org/TR/CSP/), такой код будет исполняться только в том случае, если предприняты специальные действия. А именно, необходимо передавать браузеру в HTTP-заголовке разрешение на обработку данных: директивы [src-script](https://www.w3.org/TR/CSP/#directive-script-src) с атрибутом [nonce](https://www.w3.org/TR/CSP/#framework-directive-source-list) (это требует подписывания содержимого элемента `script`) и [img-src](https://www.w3.org/TR/CSP/#directive-img-src) для обработки содержимого элемента `noscript`.

Кроме этого, Яндекс Метрика допускает другой способ подключения *кода счетчика*: вы можете разместить в HTML-коде страниц только содержимое элемента `noscript`, а содержимое элемента `script` вынести во [внешний скрипт](ru/code/install-counter-csp#separate-code-file) (например, в JS-файл).

При выборе любого способа необходимо добавить в HTTP-заголовок разрешение на обращение к Яндекс Метрике.

```
https://mc.yandex.ru
https://mc.yandex.az
https://mc.yandex.by
https://mc.yandex.co.il
https://mc.yandex.com
https://mc.yandex.com.am
https://mc.yandex.com.ge
https://mc.yandex.com.tr
https://mc.yandex.ee
https://mc.yandex.fr
https://mc.yandex.kg
https://mc.yandex.kz
https://mc.yandex.lt
https://mc.yandex.lv
https://mc.yandex.md
https://mc.yandex.tj
https://mc.yandex.tm
https://mc.yandex.uz
https://mc.webvisor.com
https://mc.webvisor.org
https://yastatic.net
wss://mc.yandex.ru
wss://mc.yandex.az
wss://mc.yandex.by
wss://mc.yandex.co.il
wss://mc.yandex.com
wss://mc.yandex.com.am
wss://mc.yandex.com.ge
wss://mc.yandex.com.tr
wss://mc.yandex.ee
wss://mc.yandex.fr
wss://mc.yandex.kg
wss://mc.yandex.kz
wss://mc.yandex.lt
wss://mc.yandex.lv
wss://mc.yandex.md
wss://mc.yandex.tj
wss://mc.yandex.tm
wss://mc.yandex.uz
wss://mc.webvisor.com
wss://mc.webvisor.org
```

```
metrika.yandex.ru
analytics.yandex.by
analytics.yandex.com
analytics.yandex.com.tr
analytics.yandex.kz
analytics.yandex.ru
metr.yandex.by
metr.yandex.com
metr.yandex.com.tr
metr.yandex.kz
metr.yandex.ru
metrica.ya.ru
metrica.yandex
metrica.yandex.by
metrica.yandex.com
metrica.yandex.com.tr
metrica.yandex.kz
metrica.yandex.ru
metrika.ya.ru
metrika.yandex
metrika.yandex.by
metrika.yandex.com
metrika.yandex.com.tr
metrika.yandex.kz
metrika.yandex.uz
```

## ru/code/install-counter-csp#nonceРазмещение кода счетчика в HTML-коде страниц сайта

Внимание

В примерах прописаны не все адреса, необходимые для работы Метрики.

- [Общий список адресов](ru/code/install-counter-csp#urls)
- [Адреса для frame-ancestors](ru/code/install-counter-csp#frame-ancestors-urls)

Если вы используете этот способ, HTTP-заголовок `Content-Security-Policy` или `Content-Security-Policy-Report-Only` должен содержать директивы:

- [script-src](https://www.w3.org/TR/CSP/#directive-script-src) с атрибутом [nonce](https://www.w3.org/TR/CSP/#framework-directive-source-list). Этот атрибут должен содержать строковое значение в виде случайной последовательности символов (латинские буквы и цифры). Это значение должно быть сформировано на сервере случайным образом отдельно при каждом запросе. Content-Security-Policy: script-src 'nonce-<последовательность символов>'; Эту же последовательность символов должен содержать атрибут `nonce` в элементе `script` кода счетчика на страницах сайта. ... <!-- Yandex Metrica tag --> <script type="text/javascript" nonce="<последовательность символов>"> (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a|| []).push(arguments)}; ...
- [img-src](https://www.w3.org/TR/CSP/#directive-img-src) — для разрешения обработки содержимого элемента `noscript`. Content-Security-Policy: img-src https://mc.yandex.ru;
- [connect-src](https://www.w3.org/TR/CSP/#directive-connect-src) — для подключения к Яндекс Метрике. Content-Security-Policy: connect-src https://mc.yandex.ru;
- [child-src](https://www.w3.org/TR/CSP/#child-src) с указанием строки `blob: https://mc.yandex.ru` для правильной работы Вебвизора, карт кликов, ссылок и скроллинга. Content-Security-Policy: child-src blob: https://mc.yandex.ru;
- [frame-src](https://www.w3.org/TR/CSP/#directive-frame-src) с указанием строки `blob: https://mc.yandex.ru` для правильной работы Вебвизора, карт кликов, ссылок и скроллинга. Content-Security-Policy: frame-src blob: https://mc.yandex.ru;
- [frame-ancestors](https://www.w3.org/TR/CSP/#directive-frame-ancestors) для правильной работы Вебвизора, карт кликов, ссылок и скроллинга. Используйте [адреса для frame-ancestors](ru/code/install-counter-csp#frame-ancestors-urls). Content-Security-Policy: frame-ancestors: http://metrika.yandex.ru;

Пример HTTP-заголовка при использовании данного способа:

```
Content-Security-Policy:
 ...
 img-src https://mc.yandex.ru;
 script-src https://mc.yandex.ru https://yastatic.net 'nonce-<последовательность символов>';
 connect-src https://mc.yandex.ru;
 ...
```

## ru/code/install-counter-csp#separate-code-fileПодключение кода счетчика с помощью внешнего скрипта

Внимание

В примерах прописаны не все адреса, необходимые для работы Метрики. [Общий список адресов](ru/code/install-counter-csp#urls)

Если вы используете этот способ, HTTP-заголовок `Content-Security-Policy` или `Content-Security-Policy-Report-Only` может иметь общий набор директив, включая правила для загрузки данных от Яндекс Метрики:

- [script-src](https://www.w3.org/TR/CSP/#directive-script-src) для разрешения обработки скриптов. Content-Security-Policy: script-src https://mc.yandex.ru https://yastatic.net;
- source: ru/_includes/code/install-counter-csp/id-nonce/dir1.md [img-src](https://www.w3.org/TR/CSP/#directive-img-src) — для разрешения обработки содержимого элемента `noscript`. Content-Security-Policy: img-src https://mc.yandex.ru; endsource: ru/_includes/code/install-counter-csp/id-nonce/dir1.md
- source: ru/_includes/code/install-counter-csp/id-nonce/dir2.md [connect-src](https://www.w3.org/TR/CSP/#directive-connect-src) — для подключения к Яндекс Метрике. Content-Security-Policy: connect-src https://mc.yandex.ru; endsource: ru/_includes/code/install-counter-csp/id-nonce/dir2.md
- source: ru/_includes/code/install-counter-csp/id-nonce/dir3.md [child-src](https://www.w3.org/TR/CSP/#child-src) с указанием строки `blob: https://mc.yandex.ru` для правильной работы Вебвизора, карт кликов, ссылок и скроллинга. Content-Security-Policy: child-src blob: https://mc.yandex.ru; endsource: ru/_includes/code/install-counter-csp/id-nonce/dir3.md
- source: ru/_includes/code/install-counter-csp/id-nonce/dir4.md [frame-src](https://www.w3.org/TR/CSP/#directive-frame-src) с указанием строки `blob: https://mc.yandex.ru` для правильной работы Вебвизора, карт кликов, ссылок и скроллинга. Content-Security-Policy: frame-src blob: https://mc.yandex.ru; endsource: ru/_includes/code/install-counter-csp/id-nonce/dir4.md

Пример HTTP-заголовка при использовании данного способа:

```
Content-Security-Policy:
 ...
 img-src https://mc.yandex.ru;
 script-src 'self' https://mc.yandex.ru https://yastatic.net;
 connect-src https://mc.yandex.ru;
 ...
```

Ниже представлен пример подключения JavaScript-кода во внешнем JS-файле. При этом в HTML-код страниц сайта необходимо добавить только элемент `script` с атрибутом `src`. Этот атрибут должен содержать путь к файлу (например, `metrika.js`).

```
<script type="text/javascript" src="/metrika.js"></script>
```

1. В интерфейсе Яндекс Метрики перейдите в раздел **Настройка** (вкладка **Счетчик**) и скопируйте из поля содержимое элемента `script`.
2. source: ru/_includes/code/separate-code-file/id-separate-code-file/7.md Добавьте этот код в файл `metrika.js`. Пример содержимого файла (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a|| []).push(arguments)}; m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t) [0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)}) (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym") ym(XXXXXXXX, "init", { id:XXXXXXXX, clickmap:true, trackLinks:true, accurateTrackBounce:true }); Где `XXXXXXXX` — номер счетчика Яндекс Метрики. endsource: ru/_includes/code/separate-code-file/id-separate-code-file/7.md
3. source: ru/_includes/code/separate-code-file/id-separate-code-file/4.md Чтобы счетчик собирал данные о посетителях, у которых отключен JavaScript, добавьте в HTML-код страниц сайта содержимое элемента `noscript`: <noscript><div><img src="https://mc.yandex.ru/watch/XXXXXXXX" style="position:absolute; left:-9999px;" alt="" /></div></noscript> endsource: ru/_includes/code/separate-code-file/id-separate-code-file/4.md

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

Код счетчика состоит из двух частей: JavaScript-кода, размещенного в элементе `script` и HTML-кода, включенного в элемент `noscript`.

### Была ли статья полезна?
