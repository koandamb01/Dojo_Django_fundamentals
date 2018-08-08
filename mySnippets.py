# Token need for all django forms
# Prevents cross-site request forgery (place it in a form on the HTML/template side of your project)
{% csrf_token %}

# TO add SESSION to your DJango project:
# In our terminal, head to the directory where manage.py resides and run the following commands:
# Need to be in same directory as manage.py file
  > python manage.py makemigrations
  > python manage.py migrate