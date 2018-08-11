# For the 3rd book, retrieve all the authors
b = Book.objects.get(id=3)
Author.objects.filter(books=b)

# For the 3rd book, remove the first author
b = Book.objects.get(id=2)
a = b.authors.first()
b.authors.remove(a)
b.save()

b = Book.objects.get(id=3)
a = b.authors.all()[0]
b.authors.remove(a)
b.save()

# For the 2nd book, add the 5th author as one of the authors
b = Book.objects.get(id=2)
a = Author.objects.get(id=5)
a.books.add(b)
a.save()

# Find all the books that the 3rd author is part of
a = Author.objects.get(id=3)
Book.objects.filter(authors=a)
