<ul class="list-unstyled">
  {% for doc in items %}
  <li>
    <a href="#doc/{{ doc.id }}">{{ doc.docTypeName }} №{{ doc.id }}, {{ doc.shopName}} <span class="label label-info">{{ doc.userFio }}</span></a>
  </li>
  {% endfor %}
</ul>