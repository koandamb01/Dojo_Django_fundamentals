# Create 3 different user accounts
User.objects.create(first_name='Momo', last_name='la', email='mo@la.com')
User.objects.create(first_name='Med', last_name='Bash', email='Baso@aa.com')
User.objects.create(first_name='Islam', last_name='DJ', email='DJ@dj.com')

# Have the first user create/upload 2 books.
re_user = User.objects.first()
Book.objects.create(name="Python", desc="Book for dummies", uploader=re_user)
Book.objects.create(name="IOS Swift", desc="Book for dummies", uploader=re_user)

# Have the second user create/upload 2 other books.
rel_user = User.objects.get(id=2)
Book.objects.create(name="PHP", desc="PHP for for life", uploader=re_user)
Book.objects.create(name="JAVA", desc="JAVA for for life", uploader=re_user)

# Have the first user like the last book and the first book
u = User.objects.first()
b1 = Book.objects.first()
u.liked_books.add(b1)
u.save()

b = Book.objects.last()
u.liked_books.add(b)
u.save()

# Have the second user like the first book and the third book
u2 = User.objects.get(id=2)
b = Book.objects.first()
u2.liked_books.add(b)
b = Book.objects.get(id=3)
u2.liked_books.add(b)
u.save()

# Display all users who like the first book
b1 = Book.objects.first()
User.objects.filter(liked_books=b1)

# Display the user who uploaded the first book
Book.objects.first().uploader

# Display all users who like the second book
b1 = Book.objects.get(id=2)
User.objects.filter(liked_books=b1)

# Display the user who uploaded the second book
Book.objects.get(id=2).uploader
