<ul class="list-unstyled">
  {% for doc in items %}
  <li>
    <a href="#doc/{{ doc.id }}">{{ doc.docType.name }} №{{ doc.id }}, {{ doc.shop.name }}</a>
  </li>
  {% endfor %}
</ul>