# ORM Commands
# Now that you have imported your models, you can use the model object to insert, delete, and modify records in your models.  For example,

Creating a new record
Blog.objects.create({{field1}}="{{value}}", {{field2}}="{{value}}", etc) # creates a new record in the Blog table
Blog.objects.create(name="Star Wars Blog", desc="Everything about Star Wars") # creates a new blog record
Blog.objects.create(name="CodingDojo Blog") # creates a new blog record with the empty desc field
Alternative way of creating a record
b = Blog(name="Disney Blog", desc="Disney stuff")
b.name = "Disney Blog!"
b.desc = "Disney stuff!!!"
b.save()
Basic Retrieval
Blog.objects.first() - retrieves the first record in the Blog table
Blog.objects.last() - retrieves the last record in the Blog table
Blog.objects.all() - retrieves all records in the Blog table
Blog.objects.count() - shows how many records are in the Blog table
Displaying records
Blog.objects.first().__dict__ - shows all the values of a single record/object as a dictionary
Blog.objects.all().values() - as shown in the videos, shows all the values of a QuerySet (QuerySet contains multiple records)
Updating the record - once you obtain an object that has the record you want to modify, use save() to update the record.  For example
b = Blog.objects.first() # gets the first record in the blogs table
b.name = "CodingDojo Blog"  # set name to be "CodingDojo Blog"
b.save() # updates the blog record
Deleting the record - use delete().  For example
b = Blog.objects.get(id=1)
b.delete() # deletes that particular record

# Other methods to retrieve records
Blog.objects.get(id=1) - retrieves where id is 1; get() retrieves one and only one record. It will return an error if it finds fewer than or more than one match.
Blog.objects.filter(name="mike") - retrieves records where name is "mike"; returns multiple records
Blog.objects.exclude(name="mike") - opposite of filter; returns multiple records
Blog.objects.order_by("created_at") - orders by created_date field
Blog.objects.order_by("-created_at") - reverses the order
Blog.objects.raw("SELECT * FROM {{app_name}}_{{class/table name}}") - performs a raw SQL query
Blog.objects.first().comments.all() - grabs all comments from the first Blog
Blog.objects.get(id=15).comments.first() - grabs the first comment from Blog id = 15
Comment.objects.get(id=15).blog.name - returns the name of the blog where Comment id = 15 belongs to
Setting Relationship
Comment.objects.create(blog=Blog.objects.get(id=1), comment="test") - create a new comment where the comment's blog points to Blog.objects.get(id=1).
Conditions
You can do a more complicated search than just if a given field is equal to a given value. Instead of just passing in the field name as a keyword argument to .get, .filter, or .exclude, you'd pass the field name__lookup type (that's a double underscore, also known as a "dunder" for people on-the-go). 

For example

Admin.objects.filter(first_name__startswith="S") - filters objects with first_name that starts with "S"
Admin.objects.exclude(first_name__contains="E") - excludes objects where first_name contains "E"
Admin.objects.filter(age__gt=80)  - filters objects with age greater than 80
Combining queries
Queries can be chained together:

admin = Admin.objects.filter(last_name__contains="o").exclude(first_name__contains="o")
admin = Admin.objects.filter(age__lt=70).filter(first_name__startswith="S")
If it's the same type of query, instead of being chained you can add multiple arguments to the function:

admin = Admin.objects.filter(age__lt=70, first_name__startswith="S")
These are cases where the conditions are joined with AND, as in, all users younger than 70 AND whose first name starts with "S". If you want OR, as in users who are younger than 70 OR whose first_name starts with "S", you can use | (the set union operator):

admin = Admin.objects.filter(age__lt=70)|Admin.objects.filter(first_name__startswith="S")
References
https://tutorial.djangogirls.org/en/django_orm/
Helpful tip
In regard to the default display when printing objects, we could create __str__ or __repr__ method in the class to handle how they want the objects to print. This is pretty handy and shows how we can leverage some of python's magic methods to make our lives easier.
class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Blog object: {} {}>".format(self.name, self.desc)
iPython - nicer looking shell
Also, if you would like, you could also install ipython (pip install ipython).  This replaces the default shell with a much nicer one (TAB indent works, line numbers, syntax highlighting, etc).