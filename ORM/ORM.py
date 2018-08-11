# ForeignKey Relationships
# To show a one-to-many relationship between models, Django uses a special field, ForeignKey. Consider these models:
# Notice that the Book model has this line: models.ForeignKey(Author, related_name="books"). This establishes a one-to-many relationship, that one author can have many books, and that information about a book's author can be accessed as some_book.author. To create a record that has this foreign key relationship, you'd pass it into the create function, like with any other field:
class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# ManyToMany Relationships
# You may remember that in order to use a many-to-many relationship in SQL, you had to construct a third, linking table with foreign key relationships to the two tables you wanted to connect. Django will do this for you automatically, if your model includes a ManyToManyField. We'll use these models as an example:
class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Publisher(models.Model):
	name = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name="publishers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



# As you can see, each publisher can publish many books, and each book can be published by many publishers. Unlike with a ForeignKey, it doesn't matter which model has the ManyToManyField. The model would still work if the Book model has a field named publishers instead.
# Adding a relationship between two existing records is simple:
this_book = Book.objects.get(id=4)
this_publisher = Publisher.objects.get(id=2)
this_publisher.books.add(this_book)



# To create a record that has this foreign key relationship, you'd pass it into the create function, like with any other field:
this_author = Author.objects.get(id=2)
my_book = Book.objects.create(title="Little Women", author=this_author)
# or on one line...
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))



# You can search based off of a ForeignKey relationship. This code will find all of the books by the author with ID 2:
this_author = Author.objects.get(id=2)
books = Book.objects.filter(author=this_author)
# one-line version:
books = Book.objects.filter(author=Author.objects.get(id=2))



# You can also search by a field in the related object by using a double underscore:
books = Book.objects.filter(author__name="Louise May Alcott")
books = Book.objects.filter(author__name__startswith="Lou")
