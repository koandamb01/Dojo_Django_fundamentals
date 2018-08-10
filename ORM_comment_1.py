# https://tutorial.djangogirls.org/en/django_orm/

Blog.objects.filter(id=2).values('name')
<QuerySet [{'name': 'Star Wars Blog'}]>

