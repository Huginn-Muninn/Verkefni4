{% extends "base.html" %}


{% block innihald %}
    <h3>Takk fyrir viðskiptin {{ nafn }}!</h3>
    <p>Kvittun hefur verið send á netfangið þitt: {{ netfang }}</p>
{% endblock %}