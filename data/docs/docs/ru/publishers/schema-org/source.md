# Яндекс Метрика

> Источник: https://yandex.ru/support/metrica/ru/publishers/schema-org/source
#### ru/publishers/schema-org/source#schema

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

#### ru/publishers/schema-org/source#identifier

**Описание свойства**

**Идентификатор**

Идентификатор позволяет Метрике отличать материалы друг от друга. Он не отображается в отчетах.

```
<meta itemprop="identifier" content="12345">
```

#### ru/publishers/schema-org/source#headline

**Описание свойства**

**Заголовок**

Заголовок может быть указан с помощью свойств [`headline`](https://schema.org/headline) или [`alternativeHeadline`](https://schema.org/alternativeHeadline) и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так:

```
<h1 itemprop="headline">В Москве побит температурный рекорд 1922 года</h1>
  <h2 itemprop="alternativeHeadline">Температура в ноябре превысила 12 °С</h2>
```

в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С».

Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства [`name`](https://schema.org/name).

#### ru/publishers/schema-org/source#alternativeHeadline

**Описание свойства**

**Заголовок**

Заголовок может быть указан с помощью свойств [`headline`](https://schema.org/headline) или [`alternativeHeadline`](https://schema.org/alternativeHeadline) и отображается в отчетах Метрики. Если заданы оба свойства, их значения будут записаны через пробел. Например, если заголовки размечены так:

```
<h1 itemprop="headline">В Москве побит температурный рекорд 1922 года</h1>
  <h2 itemprop="alternativeHeadline">Температура в ноябре превысила 12 °С</h2>
```

в отчете статья будет называться «В Москве побит температурный рекорд 1922 года Температура в ноябре превысила 12 °С».

Если не найдено ни одно из свойств выше, в качестве заголовка будет использоваться значение свойства [`name`](https://schema.org/name).

#### ru/publishers/schema-org/source#datePublished

**Описание свойства**

**Дата публикации**

Даты публикации [`datePublished`](https://schema.org/datePublished) и изменения [`dateModified`](https://schema.org/dateModified) записываются в формате [ISO 8601](https://www.iso.org/standard/40874.html).

`html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> `

или в атрибуте `datetime` тега `time`.

```
<time itemprop="dateModified" datetime="2018-12-11T07:30:00Z">10:30, 11 декабря 2018 </time>
```

#### ru/publishers/schema-org/source#dateModified

**Описание свойства**

**Дата изменения**

Даты публикации [`datePublished`](https://schema.org/datePublished) и изменения [`dateModified`](https://schema.org/dateModified) записываются в формате [ISO 8601](https://www.iso.org/standard/40874.html).

`html <meta itemprop="datePublished" content="2018-12-11T08:56:49Z" /> `

или в атрибуте `datetime` тега `time`.

```
<time itemprop="dateModified" datetime="2018-12-11T07:30:00Z">10:30, 11 декабря 2018 </time>
```

#### ru/publishers/schema-org/source#itemListElement

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

#### ru/publishers/schema-org/source#author

**Описание свойства**

**Автор**

Автор указывается с помощью свойства [`author`](https://schema.org/author). Если авторов несколько, укажите их в разных тегах.

`html <div itemprop="author">Иван Иванов</div> `

Значение также может быть взято из:

- свойства `name` класса [`Person`](https://schema.org/Person) <div itemprop="author" itemscope itemtype="http://schema.org/Person"> <span itemprop="name">Иван Иванов</span> </div>
- атрибута ссылки `href` <link itemprop='author' href="/example/authors/ivan_ivanov.html"/>

Благодаря этим данным можно посмотреть статистику по отдельным авторам в Метрике.

#### ru/publishers/schema-org/source#about

**Описание свойства**

**Тематика**

В качестве тематик можно разметить, например, ключевые слова или хэштеги. Для этого нужно определить свойство [`about`](https://schema.org/about) для каждой тематики. Значение может быть взято из свойства `name` любого класса:

```
<div itemprop="about">Жара</div>
  <div itemprop="about" itemscope itemtype="https://schema.org/Thing">
    <span itemprop="name">Москва</span>
  </div>
```

#### ru/publishers/schema-org/source#canonical

**Описание свойства**

**Каноническая ссылка**

URL материала указывается с помощью свойства [`url`](https://schema.org/url).

```
<a itemprop="url" href="https://www.example-news.com/life/weather/moscow">example-news.com</a>
```

Если не найдено свойство `url`, система будет искать каноническую ссылку. Такая ссылка используется как указание на основной материал, если текущая страница дублирует страницу на сайте. Каноническая ссылка размечается специальным атрибутом `rel="canonical"`. Например, если материал является дублем страницы `http://www.example-news.com/page`, в нем указывается `<link rel="canonical" href="http://www.example-news.com/page"/>`. В качестве URL материала будет использоваться значение атрибута `href` канонической ссылки.

Найденное значение может использоваться при генерации идентификатора материала.

#### ru/publishers/schema-org/source#mainEntityOfPage

**Описание свойства**

**Идентификатор**

Свойство будет использоваться, если не найдено свойство `identifier`. В нем ищется значение атрибута `itemid`, которое будет использоваться в качестве идентификатора.

```
<meta itemscope itemprop="mainEntityOfPage" 
   itemType="https://schema.org/WebPage" itemid="/life/weather/12345.html"/>
```

#### ru/publishers/schema-org/source#articleBody

**Описание свойства**

**Текст статьи**

В тексте определяется количество символов. Это нужно для определения объема материала. В качестве текста учитывается только содержимое вложенных тегов, символы самих тегов не учитываются. Мы рекомендуем размечать текст материала так, чтобы туда не попадало лишнее: рекламные баннеры, блоки комментариев и т. п., иначе объем материала и [показатели статистики](ru/publishers/reports/data) могут рассчитаться неправильно.

```
<p itemprop="articleBody">
   В среду, 6 ноября, в Москве был побит температурный рекорд, зафиксированный  в 1922 году. Температура воздуха составила плюс 12,1 градуса по Цельсию, как сообщает центр «Фобос».
</p>
```

Если не найдено свойство `articleBody`, в качестве текста будет использоваться значение свойств [`description`](https://schema.org/description) или [`text`](https://schema.org/text).

Если ни одно из свойств не найдено, в качестве текста берется все содержимое тега, помеченного как `Article` или `NewsArticle`, без символов тегов.

Примечание

Полную статистику можно получить по материалу, в тексте которого больше 500 символов.

[Написать в чат](https://yandex.ru/chat/#/user/036e6a02-3620-9cdc-4c5e-a34667a7379e?utm_source=spravka)

### Была ли статья полезна?
