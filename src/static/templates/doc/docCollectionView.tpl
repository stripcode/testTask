<ul class="list-unstyled">
  {% for doc in items %}
  <li>{{ doc.docType.name }} №{{ doc.id }}, {{ doc.shop.name }}</li>
  {% endfor %}
</ul>