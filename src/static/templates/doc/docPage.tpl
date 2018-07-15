<button class="btn btn-default cancelDocPage">Вернуться</button>

<h2>{{ docType.name }} №{{ id}}</h2>

<ul>
  <li>Тип документа: {{ docType.name }}</li>
  <li>Магазин: {{ shop.name }}</li>
  <li>Пользователь: {{ user.fio }}</li>
</ul>

<h4>Продукты</h4>
<ul>
{% for product in products %}
  <li>{{ product.name }}
    <br><img src="/data/product/{{ product.id }}/barcode/"
  </li>
{% endfor %}
</ul>