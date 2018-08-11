# https://tutorial.djangogirls.org/en/django_orm/

Blog.objects.filter(id=2).values('name')
<QuerySet [{'name': 'Star Wars Blog'}]>

######## To create a record that relate to another table (one to many)
dojo = Dojo.objects.last() # get the last element of my Dojo table because I want my new record to relate to that id
ninja = Ninja.objects.create(first_name="MO", last_name="Dexxk", dojo=dojo)

######## To create a ManyToMany relation between a book and author
a = Author.objects.get(id=2)
>>> b = Book.objects.first()
>>> a.add(b)
>>> a.books.add(b)


# Fetch all record and order location by asc 
Team.objects.all().order_by("team_name")

# Fetch all record and order location by desc 
Team.objects.all().order_by("-team_name")


