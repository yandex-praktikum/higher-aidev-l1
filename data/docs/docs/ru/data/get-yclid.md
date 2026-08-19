> Источник: https://yandex.ru/support/metrica/ru/data/get-yclid
# Получение yclid на сайте для отслеживания конверсий

- [Шаг 1 — Настройте сохранение yclid из URL объявлений Директа](ru/data/get-yclid#shag-1-—-nastrojte-sohranenie-yclid-iz-url-obuyavlenij-direkta)
- [Шаг 2 — Настройте извлечение значения yclid из cookie](ru/data/get-yclid#shag-2-—-nastrojte-izvlechenie-znacheniya-yclid-iz-cookie)

Параметр `yclid` добавляется в URL объявлений Яндекс Директа. Чтобы отслеживать конверсии по `yclid`, нужно настроить извлечение его значения из URL и сохранение на вашем сервере, а затем [передавать в Яндекс Метрику в CSV-файле](ru/data/offline-conversion).

Перед началом работы убедитесь, что вы можете:

- Изменять HTML-код страниц сайта так, чтобы сохранять значения параметра `yclid` из URL объявлений.
- Сохранять значение параметра `yclid` вместе с информацией о посетителях, полученной на вашем сайте.

## ru/data/get-yclid#shag-1-—-nastrojte-sohranenie-yclid-iz-url-obuyavlenij-direktaШаг 1 — Настройте сохранение yclid из URL объявлений Директа

В код страниц вашего сайта добавьте JavaScript-код для сохранения `yclid` в cookie. В примере ниже cookie присвоено имя `yclid`.

```
<script type="text/javascript">
function setCookie(name, value, days){
    var date = new Date();
    date.setTime(date.getTime() + (days*24*60*60*1000)); 
    var expires = "; expires=" + date.toGMTString();
    document.cookie = name + "=" + value + expires + ";path=/";
}
function getParam(p){
    var match = RegExp('[?&]' + p + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}
var yclid = getParam('yclid');
if(yclid){
    setCookie('yclid', yclid, 90);
}
</script> 
```

Рекомендуем поместить этот код в элемент `body`. Так вам не потребуется добавлять его каждый раз при создании рекламного объявления.

## ru/data/get-yclid#shag-2-—-nastrojte-izvlechenie-znacheniya-yclid-iz-cookieШаг 2 — Настройте извлечение значения yclid из cookie

В коде страниц сайта разместите код для извлечения и передачи `yclid` на ваш сервер. Сделать это можно на странице, на которой посетители заполняют форму и оставляют контактную информацию или другие сведения. Рекомендуем передавать `yclid` как скрытое значение поля в форме, которую заполняют посетители.

Примечание

Код для передачи `yclid` можно написать на любом языке программирования, который поддерживается вашим сервером или браузером посетителя. В примере используется JavaScript.

```
<form action="" name="myForm">   
    Name: <input type="text" name="name">
    <!--Скрытое поле для извлечения yclid-->   
    <input type="hidden" id="yclid_field" name="yclid_field" value="">    
    <input type="submit" value="Submit Form" name="btnSubmit">  
</form>

<!--Извлечение yclid и изменение скрытого поля-->
<script> 
  function readCookie(name) { 
  var n = name + "="; 
  var cookie = document.cookie.split(';'); 
  for(var i=0;i < cookie.length;i++) {      
      var c = cookie[i];      
      while (c.charAt(0)==' '){c = c.substring(1,c.length);}      
      if (c.indexOf(n) == 0){return c.substring(n.length,c.length);} 
  } 
  return null; 
  } 
  window.onload = function() {      
      document.getElementById('yclid_field').value = 
  readCookie('yclid'); 
  } 
</script>
```

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

### Была ли статья полезна?
