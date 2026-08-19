> Источник: https://yandex.ru/support/metrica/ru/publishers/schema-org/json-ld
# JSON-LD

- [Принципы разметки](ru/publishers/schema-org/json-ld#how-to)
- [Какие материалы можно разметить](ru/publishers/schema-org/json-ld#types)
- [Как разметить материал](ru/publishers/schema-org/json-ld#schemas)
- [Пример разметки](ru/publishers/schema-org/json-ld#example)
- [Узнайте больше](ru/publishers/schema-org/json-ld#uznajte-bolshe)

JSON-LD — это способ разметки, при котором данные передаются с помощью объектов [связанных данных](https://ru.wikipedia.org/wiki/Linked_data) (Linked Data, LD).

Внимание

Если вы встраиваете микроразметку с помощью плагина, вероятно, потребуется его доработка. Для этого обратитесь к разработчику плагина или другому специалисту, который обладает навыками разработки.

## ru/publishers/schema-org/json-ld#how-toПринципы разметки

Данные в формате JSON-LD описываются набором разделенных запятыми пар ключ-значение. Формат предусматривает зарезервированные ключи, с помощью которых можно определять контекст описания или связывать объекты различным образом. Например, `@context` определяет словарь объектов (в данном случае — Schema.org), а `@type` — тип описываемой сущности. Полный список зарезервированных ключей приведен в [документации JSON-LD](http://www.w3.org/TR/json-ld/#syntax-tokens-and-keywords).

Сущность описывается в фигурных скобках { } в теге `<script>` с атрибутом `type="application/ld+json"` или `type="ld+json"`. Укажите, что для разметки используется словарь Schema.org — `"@context":"http://schema.org"`. С помощью ключа `@type` укажите класс Schema.org, определяющий описываемую сущность. Разметьте свойства сущности — в качестве ключей используйте свойства заданного класса Schema.org.

Для разметки нескольких сущностей на странице вы можете использовать:

Для каждого узла графа укажите `@id` — ссылку на раздел страницы, содержащий описываемую сущность.

В примере ниже описываются две новостные статьи `"@type":"NewsArticle"`. Указаны идентификатор статьи (ключ `@id`), дата публикации (ключ `datePublished`) и авторы статьи (ключ `author`) в виде массива из двух элементов. Авторы описываются с помощью вложенных сущностей класса `Person`.

```
<script type="application/ld+json">
{  
  "@context": "http://schema.org",
  "@graph": [
    {
     "@type": "NewsArticle",
     "@id": "https://www.example-news.com/life/weather/moscow#cao",  
     "datePublished": "2018-12-11T08:56:49Z",
     "author": [{"@type": "Person", "name": "Иван Иванов"}, 
        {"@type": "Person", "name": "Петр Петров"}]
    },
    {
     "@type": "NewsArticle",
     "@id": "https://www.example-news.com/life/weather/moscow#zao",  
     "datePublished": "2018-12-11T09:56:49Z",
     "author": [{"@type": "Person", "name": "Иван Иванов"}, 
        {"@type": "Person", "name": "Алексей Алексеев"}]
    }
  ]
}
</script>
```

Для каждой сущности укажите `@id` — ссылку на раздел страницы, содержащий описываемую сущность.

В примере ниже описываются две новостные статьи `"@type":"NewsArticle"`. Указаны идентификатор статьи (ключ `@id`), дата публикации (ключ `datePublished`) и авторы статьи (ключ `author`) в виде массива из двух элементов. Авторы описываются с помощью вложенных сущностей класса `Person`.

```
<script type="application/ld+json">
[{  
  "@context": "http://schema.org",
  "@type": "NewsArticle",
  "@id": "https://www.example-news.com/life/weather/moscow#cao",  
  "datePublished": "2018-12-11T08:56:49Z",
  "author": [{"@type": "Person", "name": "Иван Иванов"}, 
     {"@type": "Person", "name": "Петр Петров"}]
 },
 {
  "@context": "http://schema.org",
  "@type": "NewsArticle",
  "@id": "https://www.example-news.com/life/weather/moscow#zao",  
  "datePublished": "2018-12-11T09:56:49Z",
  "author": [{"@type": "Person", "name": "Иван Иванов"}, 
    {"@type": "Person", "name": "Алексей Алексеев"}]
 }
]
</script>
```

[Перейти на сайт JSON-LD](http://json-ld.org/)

## ru/publishers/schema-org/json-ld#typesКакие материалы можно разметить

Метрика поддерживает разметку следующих материалов:

- Статья, новость или пост в блоге ([`Article`](https://schema.org/Article), [`NewsArticle`](https://schema.org/NewsArticle) или [`BlogPosting`](https://schema.org/BlogPosting))
- Описание фильма ([`Movie`](https://schema.org/Movie))
- Обзор или отзыв ([`Review`](https://schema.org/Review))
- Рецепт ([`Recipe`](https://schema.org/Recipe))
- Вопрос-ответ ([`Question`](https://schema.org/Question) или [`QAPage`](https://schema.org/QAPage))

Другие материалы, размеченные по стандарту, не попадут в отчеты Метрики.

## ru/publishers/schema-org/json-ld#schemasКак разметить материал

Разметьте материал в соответствии с приведенными ниже правилами, чтобы он корректно обрабатывался Метрикой. Для получения более полной статистики рекомендуем разметить все элементы материала, но обязательными являются только три — идентификатор, заголовок и текст.

Если вы уже используете JSON-LD, проверьте, соответствует ли разметка на вашем сайте этим требованиям. Примеры кода в правилах не являются единственно правильным вариантом разметки.

Разметку можно добавить на сайт автоматически — например, с помощью [плагинов для WordPress](https://wordpress.org/plugins/search/schema/). Перед использованием убедитесь, что выбранный плагин позволяет передать в код страницы все нужные элементы разметки.

Внимание

Если на одной странице несколько материалов, размечайте каждый из них отдельно, чтобы статистика собиралась правильно.

Укажите следующие элементы материала (обязательные элементы отмечены звездочкой):

| идентификатор* заголовок* текст* автор | тематика даты публикации и изменения рубрика URL материала |
| --- | --- |

**Идентификатор***

Идентификатор указывается с помощью зарезервированного ключа `@id`. Он позволяет Метрике отличать материалы друг от друга. Идентификатор не отображается в отчетах. Идентификатором может быть, например, ссылка на материал или произвольное уникальное значение.

```
"@id": "https://www.example-news.com/life/weather/moscow#cao"
```

Если ключ `@id` не был найден, система попытается найти его во вложенных сущностях в ключах [`mainEntity`](https://schema.org/mainEntity) или [`mainEntityOfPage`](https://schema.org/mainEntityOfPage).

```
<script type="application/ld+json">
  {  
    "@context": "http://schema.org",  
    "@type": "NewsArticle",  
    "mainEntityOfPage": {
           "@type": "WebPage",
           "@id": "https://www.example-news.com/life/weather/moscow#cao"
        }
  }
  </script>
```

Содержимое `@id` может использоваться для расчета [доскроллов и дочтений](ru/publishers/reports/data#def-scroll). Если в качестве идентификатора:

- Указан URL статьи, Метрика определяет фрагмент после знака # (`#fragment`). Затем ищет HTML-элемент с этим фрагментом в статье (атрибут `id="fragment"`). Если фрагмент найден, начинается расчет показателей. Так же обрабатывается [URL материала](ru/publishers/schema-org/json-ld#canonical-desc).
- Указано произвольное значение и код JSON-LD размещен в `head`, то система рассчитывает показатели по содержимому `body`. Если в `body` код размещен внутри другого HTML-элемента, то для расчета используется родительский для разметки элемент. Поэтому данные в отчете могут быть неточными. Таким же образом ведется расчет, если в [URL материала](ru/publishers/schema-org/json-ld#canonical-desc) не указан фрагмент после знака #.

**Заголовок***

Заголовок отображается в отчетах Метрики. Он может быть указан в ключах [`headline`](https://schema.org/headline) или [`alternativeHeadline`](https://schema.org/alternativeHeadline). Если найдены оба ключа, их значения будут записаны через пробел. Например, если заголовки размечены так:

```
"headline": "В Москве побит температурный рекорд 1922 года",
"alternativeHeadline": "Температура в ноябре превысила 12 °С"
```

в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С».

Если не найден ни один из ключей выше, в качестве заголовка будет использоваться значение ключа [`name`](https://schema.org/name) или [`itemReviewed`](https://schema.org/itemReviewed) (для класса [`Review`](https://schema.org/Review)).

**Текст***

Текст должен содержаться в ключе [`text`](https://schema.org/text). В тексте определяется количество символов — это нужно для определения объема материала и расчета метрик доскроллов и дочтения.

```
"text": "В среду, 6 ноября, в Москве был побит температурный рекорд, зафиксированный 
  в 1922 году. Температура воздуха составила плюс 12,1 градуса по Цельсию, 
  как сообщает центр Фобос."
```

Если ключ `text` не найден, в качестве текста будет взято:

- содержимое элемента, расположенного по якорю из значения ключа `url` или `@id`: "@context": "https://schema.org", "@type": "Article", "url": "https://www.example-news.com/life/weather/moscow#cao"
- содержимое узла, в который вложена описываемая сущность (если это не `<head>`);
- содержимое `<body>` страницы во всех остальных случаях.

При расчете объема текста символы тегов не учитываются.

Примечание

Полную статистику можно получить по материалу, в тексте которого больше 500 символов.

**Автор**

Автор указывается с помощью ключа [`author`](https://schema.org/author). Если авторов несколько, перечислите их в массиве.

```
 "author": [
    {"@type": "Person", "name": "Иван Иванов"}, 
    {"@type": "Person", "name": "Петр Петров"}
  ]
```

Если ключ не был найден, система попытается найти его во вложенных сущностях в ключах [`mainEntity`](https://schema.org/mainEntity) или [`mainEntityOfPage`](https://schema.org/mainEntityOfPage).

```
<script type="application/ld+json">
{  
  "@context": "http://schema.org",  
  "@type": "NewsArticle", 
  "@id": "12345", 
  "mainEntityOfPage": {
         "@type": "WebPage",
         "author": {"@type": "Person", "name": "Иван Иванов"} 
      }
}
</script>
```

Благодаря этим данным можно посмотреть статистику по отдельным авторам.

**Тематика**

В качестве тематик можно разметить, например, ключевые слова или хэштеги. Укажите тематики в ключе [`about`](https://schema.org/about):

```
"about": [
    {"@type": "Event", "name": "Жара"},
    {"@type": "Event", "name": "Москва"}
]
```

Тип (`@type`) передавать необязательно или укажите любой, который поддерживается стандартом.

Если не найден ключ `name`, система попытается найти значения в ключе `alternateName`.

**Даты публикации и изменения**

Даты публикации и изменения указываются в ключах [`datePublished`](https://schema.org/datePublished) и [`dateModified`](https://schema.org/dateModified). Даты записываются в формате [ISO 8601](https://www.iso.org/standard/40874.html).

```
"datePublished": "2018-12-11T08:56:49Z",
"dateModified": "2018-11-06T09:26:10+04:00"
```

**Рубрика**

Рубрика — это раздел сайта, посвященный определенной теме. Для разметки рубрики используйте ключ [`BreadcrumbList`](https://schema.org/BreadcrumbList). С его помощью описывается цепочка связанных страниц («хлебные крошки»), которая обычно заканчивается текущим материалом. Внутри `BreadcrumbList` в ключе [`itemListElement`](https://schema.org/itemListElement) должно быть определено несколько сущностей типа [`ListItem`](https://schema.org/ListItem), которые описывают текущую и более широкие рубрики.

Вложенность рубрики задается с помощью ключа `position`. Например, в рубрике «Жизнь» могут содержаться вложенные рубрики «Погода» и «Происшествия». При `"position":"1"` материал находится на верхнем уровне («Жизнь»), при `"position":"2"` — на втором («Погода»).

Рубрикой материала будет считаться значение ключа `name` с наибольшим значением `position`.

Примечание

На данный момент в статистике отображаются два уровня вложенности рубрик.

```
{
  "@context": "http://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
          "@id": "//example-news.ru/life",
          "name": "Жизнь"
        }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
          "@id": "//example-news.ru/life/weather",
          "name": "Погода"
        }
    }]
}
```

**URL материала**

URL материала должен содержаться в ключе [`url`](https://schema.org/url). Рекомендуем использовать в URL фрагмент после знака #. Он укажет системе, по какому именно материалу рассчитывать показатели.

[Идентификаторы](ru/publishers/schema-org/json-ld#identifier-desc)

```
"url": "https://www.example-news.com/life/weather/moscow#cao"
```

Если разметка верна и правильно подключен счетчик, через некоторое время по материалу начнет собираться статистика в Метрике.

## ru/publishers/schema-org/json-ld#exampleПример разметки

Ниже вы можете посмотреть пример разметки [новости](https://schema.org/NewsArticle).

```
<script type="application/ld+json">
{
   "@context": "http://schema.org",
   "@graph": [
       {
         "@type":"BreadcrumbList",
         "itemListElement": [
             {
               "@type": "ListItem",
               "position": 1,
               "item": {
                 "@id": "//example-news.ru/life",
                 "name": "Жизнь"
                }
              },
              {
                 "@type": "ListItem",
                 "position": 2,
                 "item": {
                     "@id": "//example-news.ru/life/weather",
                     "name": "Погода"
                 }
               }
            ]
        },
        {
          "@type": "NewsArticle",
          "@id": "https://www.example-news.com/life/weather/moscow#cao",
          "headline": "В Москве побит температурный рекорд 1922 года",
          "alternativeHeadline": "Температура в ноябре превысила 12 °С",
          "datePublished": "2018-12-11T08:56:49Z",
          "dateModified": "2018-11-06T09:26:10+04:00",
          "text": "В среду, 6 ноября, в Москве был побит температурный рекорд, зафиксированный 
          в 1922 году. Температура воздуха составила плюс 12,1 градуса по Цельсию, 
          как сообщает центр Фобос.",
          "author": [
              {"@type": "Person", "name": "Иван Иванов"}, 
              {"@type": "Person", "name": "Петр Петров"}
           ],
          "about": {
              "@type": "Event",
              "name": "Москва"
          },
          "url": "https://www.example-news.com/life/weather/moscow#cao"
        }
    ]
}
</script>
        
```

## ru/publishers/schema-org/json-ld#uznajte-bolsheУзнайте больше

- [Отчеты по контенту](ru/publishers/reports/main)

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

Обратите внимание: служба поддержки не обзванивает пользователей. Не следуйте указаниям людей, которые вам звонят и представляются службой поддержки Яндекс Метрики.

| Полезные ссылки Демосчетчик Добавить счетчик Плагины для CMS Бесплатная настройка счетчика API Яндекс Метрики Предложить идею Обсудить в Telegram | Онлайн-обучение Получить сертификат по Яндекс Метрике Пройти обучающий курс |
| --- | --- |

| itemprop | Описание свойства |
| --- | --- |
| Классы Article и NewsArticle |  |
| identifier типа PropertyValue , или Text , или URL | Идентификатор Идентификатор позволяет Метрике отличать материалы друг от друга. Он не отображается в отчетах. < meta itemprop = "identifier" content = "12345" > |
| mainEntityOfPage типа URL , CreativeWork | Идентификатор Свойство будет использоваться, если не найдено свойство identifier . В нем ищется значение атрибута itemid , которое будет использоваться в качестве идентификатора. < meta itemscope itemprop = "mainEntityOfPage" itemType = "https://schema.org/WebPage" itemid = "/life/weather/12345.html" /> |
| headline типа Text | Заголовок Заголовок может быть указан с помощью свойств headline или alternativeHeadline и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так: < h1 itemprop = "headline" > В Москве побит температурный рекорд 1922 года </ h1 > < h2 itemprop = "alternativeHeadline" > Температура в ноябре превысила 12 °С </ h2 > в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С». Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства name . |
| alternativeHeadline типа Text | Заголовок Заголовок может быть указан с помощью свойств headline или alternativeHeadline и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так: < h1 itemprop = "headline" > В Москве побит температурный рекорд 1922 года </ h1 > < h2 itemprop = "alternativeHeadline" > Температура в ноябре превысила 12 °С </ h2 > в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С». Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства name . |
| articleBody типа Text | Текст статьи В тексте определяется количество символов. Это нужно для определения объема материала. В качестве текста учитывается только содержимое вложенных тегов, символы самих тегов не учитываются. Мы рекомендуем размечать текст материала так, чтобы туда не попадало лишнее: рекламные баннеры, блоки комментариев и т. п., иначе объем материала и показатели статистики могут рассчитаться неправильно. < p itemprop = "articleBody" > В среду, 6 ноября, в Москве был побит температурный рекорд, зафиксированный в 1922 году. Температура воздуха составила плюс 12,1 градуса по Цельсию, как сообщает центр «Фобос». </ p > Если не найдено свойство articleBody , в качестве текста будет использоваться значение свойств description или text . Если ни одно из свойств не найдено, в качестве текста берется все содержимое тега, помеченного как Article или NewsArticle , без символов тегов. Примечание Полную статистику можно получить по материалу, в тексте которого больше 500 символов. |
| author типа Text , или Person , или Organization | Автор Автор указывается с помощью свойства author . Если авторов несколько, укажите их в разных тегах. html <div itemprop="author">Иван Иванов</div> Значение также может быть взято из: свойства name класса Person < div itemprop = "author" itemscope itemtype = "http://schema.org/Person" > < span itemprop = "name" > Иван Иванов </ span > </ div > атрибута ссылки href < link itemprop = 'author' href = "/example/authors/ivan_ivanov.html" /> Благодаря этим данным можно посмотреть статистику по отдельным авторам в Метрике. |
| about типа Thing | Тематика В качестве тематик можно разметить, например, ключевые слова или хэштеги. Для этого нужно определить свойство about для каждой тематики. Значение может быть взято из свойства name любого класса: < div itemprop = "about" > Жара </ div > < div itemprop = "about" itemscope itemtype = "https://schema.org/Thing" > < span itemprop = "name" > Москва </ span > </ div > |
| datePublished типа Date | Дата публикации Даты публикации datePublished и изменения dateModified записываются в формате ISO 8601 . html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> или в атрибуте datetime тега time . < time itemprop = "dateModified" datetime = "2018-12-11T07:30:00Z" > 10:30, 11 декабря 2018 </ time > |
| dateModified типа Date | Дата изменения Даты публикации datePublished и изменения dateModified записываются в формате ISO 8601 . html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> или в атрибуте datetime тега time . < time itemprop = "dateModified" datetime = "2018-12-11T07:30:00Z" > 10:30, 11 декабря 2018 </ time > |
| Класс BreadcrumbList |  |
| itemListElement типа ListItem , или Text , или Thing | Рубрика Рубрика — это раздел сайта, посвященный определенной теме. Для разметки рубрики используйте класс BreadcrumbList . С его помощью описывается цепочка связанных страниц («хлебные крошки»), которая обычно заканчивается текущим материалом. Внутри BreadcrumbList должно быть определено несколько сущностей типа ListItem , размеченных свойством itemListElement , которые описывают текущую и более широкие рубрики. Вложенность рубрик задается с помощью свойства position класса ListItem . Например, в рубрике «Жизнь» могут содержаться вложенные рубрики «Погода» и «Происшествия». При position = '1' материал находится на верхнем уровне («Жизнь»), при position = '2' — на втором («Погода»). Рубрикой материала будет считаться значение свойства name сущности ListItem с наибольшим значением position . Примечание На данный момент в статистике отображаются два уровня вложенности рубрик. < ol itemscope itemtype = "http://schema.org/BreadcrumbList" > < li itemprop = "itemListElement" itemscope itemtype = "http://schema.org/ListItem" > < a itemprop = "item" href = "//example-news.ru/life" > < span itemprop = "name" > Жизнь </ span > </ a > < meta itemprop = "position" content = "1" /> </ li > < li itemprop = "itemListElement" itemscope itemtype = "http://schema.org/ListItem" > < a itemprop = "item" href = "//example-news.ru/life/weather" > < span itemprop = "name" > Погода </ span > </ a > < meta itemprop = "position" content = "2" /> </ li > </ ol > |
| Другое |  |
|  | Каноническая ссылка URL материала указывается с помощью свойства url . < a itemprop = "url" href = "https://www.example-news.com/life/weather/moscow" > example-news.com </ a > Если не найдено свойство url , система будет искать каноническую ссылку. Такая ссылка используется как указание на основной материал, если текущая страница дублирует страницу на сайте. Каноническая ссылка размечается специальным атрибутом rel="canonical" . Например, если материал является дублем страницы http://www.example-news.com/page , в нем указывается <link rel="canonical" href="http://www.example-news.com/page"/> . В качестве URL материала будет использоваться значение атрибута href канонической ссылки. Найденное значение может использоваться при генерации идентификатора материала. |

**Описание свойства**

**Идентификатор**

Идентификатор позволяет Метрике отличать материалы друг от друга. Он не отображается в отчетах.

```
<meta itemprop="identifier" content="12345">
```

**Описание свойства**

**Заголовок**

Заголовок может быть указан с помощью свойств [`headline`](https://schema.org/headline) или [`alternativeHeadline`](https://schema.org/alternativeHeadline) и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так:

```
<h1 itemprop="headline">В Москве побит температурный рекорд 1922 года</h1>
  <h2 itemprop="alternativeHeadline">Температура в ноябре превысила 12 °С</h2>
```

в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С».

Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства [`name`](https://schema.org/name).

**Описание свойства**

**Заголовок**

Заголовок может быть указан с помощью свойств [`headline`](https://schema.org/headline) или [`alternativeHeadline`](https://schema.org/alternativeHeadline) и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так:

```
<h1 itemprop="headline">В Москве побит температурный рекорд 1922 года</h1>
  <h2 itemprop="alternativeHeadline">Температура в ноябре превысила 12 °С</h2>
```

в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С».

Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства [`name`](https://schema.org/name).

**Описание свойства**

**Дата публикации**

Даты публикации [`datePublished`](https://schema.org/datePublished) и изменения [`dateModified`](https://schema.org/dateModified) записываются в формате [ISO 8601](https://www.iso.org/standard/40874.html).

`html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> `

или в атрибуте `datetime` тега `time`.

```
<time itemprop="dateModified" datetime="2018-12-11T07:30:00Z">10:30, 11 декабря 2018 </time>
```

**Описание свойства**

**Дата изменения**

Даты публикации [`datePublished`](https://schema.org/datePublished) и изменения [`dateModified`](https://schema.org/dateModified) записываются в формате [ISO 8601](https://www.iso.org/standard/40874.html).

`html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> `

или в атрибуте `datetime` тега `time`.

```
<time itemprop="dateModified" datetime="2018-12-11T07:30:00Z">10:30, 11 декабря 2018 </time>
```

**Описание свойства**

**Рубрика**

Рубрика — это раздел сайта, посвященный определенной теме. Для разметки рубрики используйте класс [`BreadcrumbList`](https://schema.org/BreadcrumbList). С его помощью описывается цепочка связанных страниц («хлебные крошки»), которая обычно заканчивается текущим материалом. Внутри `BreadcrumbList` должно быть определено несколько сущностей типа [`ListItem`](https://schema.org/ListItem), размеченных свойством [`itemListElement`](https://schema.org/itemListElement), которые описывают текущую и более широкие рубрики.

Вложенность рубрик задается с помощью свойства `position` класса `ListItem`. Например, в рубрике «Жизнь» могут содержаться вложенные рубрики «Погода» и «Происшествия». При `position = '1'` материал находится на верхнем уровне («Жизнь»), при `position = '2'` — на втором («Погода»).

Рубрикой материала будет считаться значение свойства `name` сущности `ListItem` с наибольшим значением `position` .

Примечание

На данный момент в статистике отображаются два уровня вложенности рубрик.

```
<ol itemscope itemtype="http://schema.org/BreadcrumbList">
   <li itemprop="itemListElement" itemscope
       itemtype="http://schema.org/ListItem">
     <a itemprop="item" href="//example-news.ru/life">
     <span itemprop="name">Жизнь</span></a>
     <meta itemprop="position" content="1" />
   </li>
   <li itemprop="itemListElement" itemscope
       itemtype="http://schema.org/ListItem">
     <a itemprop="item" href="//example-news.ru/life/weather">
     <span itemprop="name">Погода</span></a>
     <meta itemprop="position" content="2" />
   </li>
 </ol>
```

**Описание свойства**

**Автор**

Автор указывается с помощью свойства [`author`](https://schema.org/author). Если авторов несколько, укажите их в разных тегах.

`html <div itemprop="author">Иван Иванов</div> `

Значение также может быть взято из:

- свойства `name` класса [`Person`](https://schema.org/Person) <div itemprop="author" itemscope itemtype="http://schema.org/Person"> <span itemprop="name">Иван Иванов</span> </div>
- атрибута ссылки `href` <link itemprop='author' href="/example/authors/ivan_ivanov.html"/>

Благодаря этим данным можно посмотреть статистику по отдельным авторам в Метрике.

**Описание свойства**

**Тематика**

В качестве тематик можно разметить, например, ключевые слова или хэштеги. Для этого нужно определить свойство [`about`](https://schema.org/about) для каждой тематики. Значение может быть взято из свойства `name` любого класса:

```
<div itemprop="about">Жара</div>
  <div itemprop="about" itemscope itemtype="https://schema.org/Thing">
    <span itemprop="name">Москва</span>
  </div>
```

**Описание свойства**

**Каноническая ссылка**

URL материала указывается с помощью свойства [`url`](https://schema.org/url).

```
<a itemprop="url" href="https://www.example-news.com/life/weather/moscow">example-news.com</a>
```

Если не найдено свойство `url`, система будет искать каноническую ссылку. Такая ссылка используется как указание на основной материал, если текущая страница дублирует страницу на сайте. Каноническая ссылка размечается специальным атрибутом `rel="canonical"`. Например, если материал является дублем страницы `http://www.example-news.com/page`, в нем указывается `<link rel="canonical" href="http://www.example-news.com/page"/>`. В качестве URL материала будет использоваться значение атрибута `href` канонической ссылки.

Найденное значение может использоваться при генерации идентификатора материала.

### Была ли статья полезна?
