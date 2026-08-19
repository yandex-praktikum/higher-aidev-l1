> Источник: https://yandex.ru/support/metrica/ru/general/safari-cookie
# Настройка сервера для работы с Safari

- [Логика обновления cookie](ru/general/safari-cookie#logic)
- [Инструкция для сервера nginx](ru/general/safari-cookie#example)[Простой способ](ru/general/safari-cookie#simple)[Продвинутый способ](ru/general/safari-cookie#advanced)[Завершающие шаги](ru/general/safari-cookie#end)

Для улучшения сбора данных и таргетинга рекламы в браузере Safari необходимо настроить обновление cookie `_ym_uid` на сервере. Этот тип cookie помогает идентифицировать посетителей сайта.

## ru/general/safari-cookie#logicЛогика обновления cookie

Если в заголовке запроса `Cookie` присутствует `_ym_uid`, сервер должен отправить `Set-Cookie` с тем же значением `_ym_uid` и установить срок его действия на 1 год.

Аналогично с `_ym_d` — этот cookie-файл содержит время создания `_ym_uid`.

## ru/general/safari-cookie#exampleИнструкция для сервера nginx

Сначала отредактируйте файл конфигурации nginx.

Примечание

Путь к файлам конфигурации может отличаться в зависимости от настроек вашего сервера.

```
sudo nano /etc/nginx/sites-enabled/default
```

### ru/general/safari-cookie#simpleПростой способ

Внимание

Если вы используете директиву `add_header` для установки других заголовков или `if` для условного роутинга, этот способ вам не подходит. Необходимо использовать продвинутый способ во избежание [нежелательного поведения](https://www.f5.com/company/blog/nginx/avoiding-top-10-nginx-configuration-mistakes#if).

В каждом блоке `location` добавьте следующий код (его можно разместить в любом месте блока):

Примечание

Если ваш сервис не использует протокол HTTPS, удалите из заголовка параметр `Secure;`.

Если ваш сервис использует субдомены, используйте корневой домен вместо переменной `$host` (например, `example.com` для сайта `sales.example.com`).

```
# Обновление куки Яндекс Метрики

if ($cookie__ym_uid) {
    set $ym_postfix "Max-Age=31536000;Secure;Path=/;Domain=.$host";

    add_header Set-Cookie "_ym_uid=$cookie__ym_uid;$ym_postfix";
    add_header Set-Cookie "_ym_d=$cookie__ym_d;$ym_postfix";
    add_header Set-Cookie "_ym_ucs=nginx;$ym_postfix";
}
```

### ru/general/safari-cookie#advancedПродвинутый способ

Примечание

Название пакета и способ установки могут отличаться на вашем сервере.

1. Установите модуль `lua` для nginx. sudo apt install libnginx-mod-http-lua
2. В каждом блоке `server` добавьте следующий код (его можно разместить в любом месте блока): Примечание Если ваш сервис не использует протокол HTTPS, удалите из заголовка параметр `Secure;`. Если ваш сервис использует субдомены, используйте корневой домен в кавычках вместо переменной `ngx.var.host` (например, `example.com` для сайта `sales.example.com`). # Обновление куки Яндекс Метрики header_filter_by_lua_block { if ngx.var.cookie__ym_uid and ngx.var.host then local ym_postfix = "Max-Age=31536000; Secure; Path=/; Domain=." .. ngx.var.host ngx.header["Set-Cookie"] = { "_ym_uid=" .. ngx.var.cookie__ym_uid .. "; " .. ym_postfix, "_ym_d=" .. (ngx.var.cookie__ym_d or "") .. "; " .. ym_postfix, "_ym_ucs=nginx; " .. ym_postfix } end }

### ru/general/safari-cookie#endЗавершающие шаги

Проверьте корректность конфигурации:

```
sudo nginx -t
```

После проверки обновите конфигурацию nginx:

```
sudo service nginx reload
```

Чтобы проверить, правильно ли настроен сервер:

1. В браузере Safari откройте ваш сайт.
2. В меню выберите **Safari** → **Настройки** (**Settings**).
3. На вкладке **Дополнительно** (**Advanced**) поставьте галочку **Показывать функции для веб-разработчиков** (**Show features for web developers**).
4. Откройте режим разработчика с помощью клавиш `Cmd+Opt+I` и перезагрузите страницу.
5. В режиме разработки выберите пункт **Разработка** (**Network**) в меню.
6. Найдите первый запрос и проверьте, что заголовок выставляется в поле **Ответ** (**Response**).

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
