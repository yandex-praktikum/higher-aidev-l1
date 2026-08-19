> Источник: https://yandex.ru/support/metrica/ru/objects/method-sprav
# Справочник методов предыдущей версии

В Яндекс Метрике обновился код счетчика, а также [методы JavaScript API](ru/objects/method-reference). Ниже представлена предыдущая версия методов.

Отслеживание загрузки файлов с заданными расширениями.

```
addFileExtension(extensions)
```

Параметр `extensions` соответствует параметру [новой версии метода](ru/objects/addfileextension).

Отправка информации о переходе по внешней ссылке.

```
extLink(url[, options])
```

Параметры `url` и `options` соответствуют параметрам [новой версии метода](ru/objects/extlink).

Отправка информации о загрузке файла.

```
file(url[, options])
```

Параметры `url` и `options` соответствуют параметрам [новой версии метода](ru/objects/file).

Получение идентификатора посетителя сайта, заданного Яндекс Метрикой.

```
yaCounterXXXXXXXX.getClientID()
```

Отправка данных о просмотре.

```
hit(url[, options])
```

Пример:

```
var yaCounterXXXXXXXX = new Ya.Metrika({id: XXXXXXXX});
//...
yaCounterXXXXXXXX.hit('#!contacts', {
    title: 'Контактная информация',
    referer: 'http://example.com/#!main'
});
```

Параметры `url` и `options` соответствуют параметрам [новой версии метода](ru/objects/hit).

Передача информации о том, что визит пользователя не является отказом.

```
notBounce([options])
```

Параметр `options` соответствует параметру [новой версии метода](ru/objects/notbounce).

Передача произвольных [параметров визита](ru/data/visit-params-data).

```
params(parameters)
```

Примеры передачи параметров визита:

```
var yaParams = {
    x: 10,
    y: "неавторизованный пользователь"
}

var yaCounterXXXXXXXX = new Ya.Metrika({id: XXXXXXXX, params: window.yaParams||{}});
```

Допустим, необходимо определить, как цвет кнопки **Купить** влияет на конверсию по цели «Переход в корзину».

Если пользователю показывается красная кнопка, определяем параметр:

```
var yaParams = {ab_test: "красная кнопка"};
```

Если пользователю показывается зеленая кнопка, определяем параметр:

```
var yaParams = {ab_test: "зеленая кнопка"};
```

Передаем этот параметр любым удобным способом. Например, при инициализации счетчика на страницах с товаром или с помощью метода reachGoal, вызываемого при нажатии кнопки **Купить**.

```
var yaParams = {
    "level1":{"level2":["level3_1","level3_2"]}}
...
```

Параметр `parameters` соответствует параметру [новой версии метода](ru/objects/params-method).

Передача информации о достижении [цели](ru/general/goals).

```
reachGoal(target[, params[, callback[, ctx]]])
```

Примеры установки цели:

```
...
<form action="" method="get" onsubmit="yaCounterXXXXXXXX.reachGoal('TARGET_NAME'); return true;">
    ...
</form>
...
```

```
...
<form action="">
    ...
    <input type="button" onclick="yaCounterXXXXXXXX.reachGoal('TARGET_NAME'); return true;" value="Заказать" />
</form>
...
```

```
...
<a href="/price.zip" onclick="yaCounterXXXXXXXX.reachGoal('TARGET_NAME'); return true;">Прайс</a>
...
```

```
...
<script type="text/javascript">
    var goalParams = {myParam: 123};
    function goalCallback () {
        console.log('запрос в Метрику успешно отправлен');
    }
</script>
<a href="/price.zip" onclick="yaCounterXXXXXXXX.reachGoal('TARGET_NAME', goalParams, goalCallback); return true;">Прайс</a>
...
```

Если вы используете **асинхронный** код счетчика и цель вызывается с помощью элемента `script`, разместите в любой части страницы следующий код:

**Решение 1**

```
<script type="text/javascript">
    window.onload = function() {
        yaCounterXXXXXXXX.reachGoal('TARGET_NAME')
    }
</script>
```

**Решение 2 (для jQuery)**

```
<script type="text/javascript">
    $(window).load(function() {
        yaCounterXXXXXXXX.reachGoal('TARGET_NAME')
    });
</script>
```

```
...
<script type="text/javascript">
    var goalParams =
    {
       order_price: 1000.35,
       currency: "RUB"
    }
</script>
<form action="" method="get" onsubmit="yaCounterXXXXXXXX.reachGoal('TARGET_NAME', goalParams); return true;">
    ...
</form>
...
```

Параметры `target`, `params`, `callback` и `ctx` соответствуют [новой версии метода](ru/objects/reachgoal).

Передача идентификатора посетителя сайта, заданного владельцем сайта.

```
yaCounterXXXXXX.setUserID("12345")
```

Передача произвольных параметров посетителей сайта.

```
userParams(parameters)
```

Параметр `parameters` соответствует параметру [новой версии метода](ru/objects/user-params).

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

### Была ли статья полезна?
