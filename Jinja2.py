# for through a list in reverse order
{% for session in request.session.activities reversed %}
    {{ session|safe }} # safe is used to render html in the vaiable
{% endfor %}