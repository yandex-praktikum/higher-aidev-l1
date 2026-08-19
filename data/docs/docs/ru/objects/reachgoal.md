> Источник: https://yandex.ru/support/metrica/ru/objects/reachgoal
# reachGoal

- [Примеры](ru/objects/reachgoal#reach_goal_examples)[Узнайте больше](ru/objects/reachgoal#uznajte-bolshe)

Важно

Для работы с JavaScript API необходимы навыки работы с HTML и JavaScript. Если вы не обладаете такими навыками, обратитесь к разработчику или вебмастеру вашего сайта.

Передача информации о достижении [цели](ru/general/goals).

```
ym(XXXXXXXX, 'reachGoal', target[, params[, callback[, ctx]]]);
```

| Параметр | Значение по умолчанию | Тип | Описание |
| --- | --- | --- | --- |
| target * | — | String | Идентификатор цели. Задается на странице редактирования счетчика при создании или изменении цели типа «JavaScript-событие» |
| params | — | Object | Параметры визита |
| callback | — | Function | Callback-функция, вызываемая после отправки данных о просмотре |
| ctx | — | Object | Контекст, доступный в callback-функции по ключевому слову this |
| Поля объекта params : |  |  |  |
| order_price или price | — | Double | Цена цели . Можно указать доход в валюте или в условных единицах |
| currency | — | String | Используйте это поле, если хотите передать цену цели в валюте. Метрика распознает трехбуквенный код валюты по ISO 4217 . Если передается другая валюта, будут отправлены нулевые значения вместо валюты и суммы |

Если вы хотите отслеживать одно и то же действие в нескольких местах, достаточно [создать](ru/general/goal-js-event) одну цель типа [JavaScript-событие](ru/general/goal-js-event) и вызывать метод `reachGoal` с идентификатором этой цели каждый раз, когда она достигнута.

Если же у вас есть несколько разных событий, создайте отдельную цель для каждого события и отслеживайте их раздельно. В этом случае у целей должны быть разные идентификаторы.

Внимание

При задании идентификатора цели не используйте следующие символы: / \ & # ? = ". Если вы хотите добавить в идентификатор символ +, вместо него укажите `%2B`.

## ru/objects/reachgoal#reach_goal_examplesПримеры

Варианты установки цели в исходном коде вашей страницы:

```
...
<form action="" method="get" onsubmit="ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME'); return true;">
    ...
</form>
...
```

```
...
<form action="">
    ...
    <input type="button" onclick="ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME'); return true;" value="Заказать" />
</form>
...
```

```
...
<a href="/price.zip" onclick="ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME'); return true;">Прайс</a>
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
<a href="/price.zip" onclick="ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME', goalParams, goalCallback); return true;">Прайс</a>
...
```

Если вы используете **асинхронный** код счетчика и цель вызывается с помощью элемента `script`, разместите в любой части страницы следующий код:

```
<script type="text/javascript">
    window.onload = function() {
        ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME')
    }
</script>
```

```
<script type="text/javascript">
    $(window).load(function() {
        ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME')
    });
</script>
```

```
...
<form action="">
    ...
    <input type="button" onclick="ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME', {order_price: '1000.35', currency: 'RUB'}); return true;" value="Заказать"/>
</form>
...
```

Чтобы в качестве `order_price` передавать доход со всех странниц сайта, на которых он задан атрибутом-селектором (например, `class` или `id`), передавайте в Метрику вместе с данными о доходе имя селектора.

1. Найдите в коде вашего сайта фрагмент, где задан подобный селектор. Пример: <div class="ORDER">Сумма заказа: <div class="PRICE">110</div> рублей</div>
2. В код элемента, который будет передавать в Метрику доход по цели, добавьте имя селектора. Пример: <input type="button" onclick="ym(XXXXXXXX, 'reachGoal', 'BUY', {order_price: document.querySelector('.PRICE')?.textContent}); return true;" value="Заказать" />

```
<script type="text/javascript">
    jQuery(document).ready(function () {
      var reachGoalWithDynamicPrice = function () {
        var dynamicPrice = jQuery('#cart .price-input').reduce(function (total, input) {
          var price = parseFloat(input.val())
          
          return isNaN(price) ? total : total + price
        }, 0)
        var goalParams = {
          order_price: dynamicPrice,
          currency: "RUB"
        }
    
        ym(XXXXXXXX, 'reachGoal', 'TARGET_NAME', goalParams)
        
        return true
      }
      jQuery('#cart').submit(reachGoalWithDynamicPrice)
    }
</script>
<form id="cart" action="/submit_order.php" method="post">
    <div class="item">
      <div class="name">Дакимакура с JoJo</div>
      <div class="price">3000.5 руб</div>
      <input class="price-input hidden" value="3000.5" />
    </div>
    ...
</form>
```

- `XXXXXXXX` — номер вашего счетчика;
- `TARGET_NAME` — идентификатор цели.

### ru/objects/reachgoal#uznajte-bolsheУзнайте больше

- [Как правильно настроить reachGoal в формах](https://yandex.ru/blog/metrika-club/kak-pravilno-nastroit-reachgoal-v-formakh)

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Выберите вопрос, чтобы найти решение.

Цели в Яндекс Метрике работают одинаково для всех источников. Возможно, ни один посетитель из интересующего вас источника еще не достиг цель.

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

Это может происходить по следующим причинам:

- В Яндекс Метрике условие цели не охватывает все возможные варианты. Например, цель настроена на посещение страницы с подтверждением заказа, а на сайте еще есть возможность оформить быстрый заказ.
- У посетителя сайта в браузере установлен плагин, блокирующий работу счетчика.
- У посетителя подключен антивирус с жесткими настройками приватности.
- У посетителя низкоскоростное интернет-подключение, из-за которого на целевой странице не загрузился счетчик.

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

Обязательный параметр.

### Была ли статья полезна?
