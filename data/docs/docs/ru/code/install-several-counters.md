> Источник: https://yandex.ru/support/metrica/ru/code/install-several-counters
# Установка нескольких счетчиков на сайт

Иногда возникает необходимость разместить на странице сразу несколько счетчиков. Код вставки изображений, использующийся при отключенном JavaScript, можно разместить внутри единственного элемента `noscript`.

При установке нескольких счетчиков подключите Вебвизор только к одному счетчику, указанному в коде.

Для инициализации счетчиков используется параметр `ssr`.

```
<!-- Yandex Metrica tag -->
<script type="text/javascript">
    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=XXXXXXXX', 'ym');

ym(XXXXXXXX, 'init', {ssr:true, webvisor:true, clickmap:true, accurateTrackBounce:true, trackLinks:true});

    (function(m,e,t,r,i,k,a){
        m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
        m[i].l=1*new Date();
        for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
        k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
    })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=YYYYYYY', 'ym');

ym(YYYYYYY, 'init', {ssr:true, clickmap:true, accurateTrackBounce:true, trackLinks:true});

</script>
<noscript>
  <div>
    <img src="https://mc.yandex.ru/watch/XXXXXXXX" style="..." alt="" />
  </div>
  <div>
    <img src="https://mc.yandex.ru/watch/YYYYYYYY" style="..." alt="" />
  </div>
</noscript>
<!-- Yandex Metrica tag -->
```

Здесь `XXXXXXXX` и `YYYYYYYY` — номера счетчиков Метрики.

```
<!-- Yandex Metrica tag -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

ym(XXXXXXXX, "init", {clickmap:true, trackLinks:true, accurateTrackBounce:true});
ym(YYYYYYYY, "init", {clickmap:true, trackLinks:true, accurateTrackBounce:true, webvisor: true});

</script>
<noscript>
  <div>
    <img src="https://mc.yandex.ru/watch/XXXXXX" style="..." alt="" />
    <img src="https://mc.yandex.ru/watch/YYYYYY" style="..." alt="" />
  </div>
</noscript>
<!-- /Yandex.Metrika counter -->
```

Здесь `XXXXXXXX` и `YYYYYYYY` — номера счетчиков Метрики.

Если на одной странице установлено несколько счетчиков, один из которых загружается с параметром `ssr: true`, при некоторых сочетаниях настроек возможны проблемы с использованием Вебвизора.

Например, на странице настроены два счетчика:

- Счетчик `XXXXXXXX` установлен с параметром `ssr: true`. В настройках этого счетчика Вебвизор выключен.
- Счетчик `YYYYYYYY` установлен обычным образом и использует отложенную загрузку, например, с помощью функции `setTimeout`. В настройках этого счетчика Вебвизор включен.

В этом случае Вебвизор не будет работать на обоих счетчиках. Это происходит из-за особенностей загрузки кода:

1. Код первого счетчика формируется на сервере (это определяет параметр `ssr: true`). В этом случае загружать или не загружать Вебвизор зависит от настроек в интерфейсе Метрики.
2. В настройках Метрики Вебвизор выключен, поэтому загружаемый файл счетчика `tag.js` не будет содержать модуль Вебвизора.
3. Второй счетчик загружается после первого. Если его код инициализации не имеет параметра `ssr: true`, он загрузит тот же `tag.js`, что был сформирован для первого счетчика.
4. Соответственно, `tag.js` не будет содержать код Вебвизора и работа Вебвизора будет невозможна.

Чтобы Вебвизор работал корректно на счетчике `YYYYYYYY` нужно:

1. В настройках счетчика `XXXXXXXX` включить Вебвизор.
2. В коде инициализации счетчика `XXXXXXXX` добавить параметр `webvisor: false`.

В этом случае файл `tag.js` будет содержать код Вебвизора, но работа Вебвизора в первом счетчике будет запрещена параметром `webvisor: false`.

Пример кода для счетчика `XXXXXXXX`:

```
ym(XXXXXXXX, "init", {
    ssr: true,
    webvisor: false,
    // другие параметры
});
```

## ru/code/install-several-counters#uznajte-bolsheУзнайте больше

- [Гид по Метрике: как создать счетчик Метрики](https://yandex.ru/blog/metrika-club/gid-po-metrike-kak-sozdat-schetchik-metriki)
- [Гид по Метрике: как установить счетчик Метрики](https://yandex.ru/blog/metrika-club/gid-po-metrike-ustanovka-schetchika)
- [Гид по Метрике: настройки счетчика](https://yandex.ru/blog/metrika-club/gid-po-metrike-nastroyki-schetchika)

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

### Была ли статья полезна?
