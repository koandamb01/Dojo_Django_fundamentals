# https://tutorial.djangogirls.org/en/django_orm/

Blog.objects.filter(id=2).values('name')
<QuerySet [{'name': 'Star Wars Blog'}]>

######## To create a record that relate to another table (one to many)
dojo = Dojo.objects.last() # get the last element of my Dojo table because I want my new record to relate to that id
ninja = Ninja.objects.create(first_name="MO", last_name="Dexxk", dojo=dojo)

