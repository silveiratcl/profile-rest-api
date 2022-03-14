# Profiles REST API

Profiles REST API course code.

### Setting up development env



### Setting the project

### Creating a development server

bash
vagrant up
vagrant ssh
source ~/env/bin/activate
cd /vagrant

python manage.py runserver 0.0.0.0:8000

### Creating a django app

### Setting up the DataBase

### Api Views

1. APIview
    Describe logic to make API endpoint
API view allows to use the standar HTTP methods for functions.
+ get - return one or more itens
+ post - create an item
+ put - update an item
+ patch - partially update an item

APIviews give the most control over the logic:
+ perfect for imprementing complex logic
+ Calling other APIs
+ Working with local files

When to use APIviews:
+ Nees full control over the logic
+ Porcessing file and rendering a sychronous response
+ You are calling other APIs/servieces
+ Acessing local files or data

### Create the first API View

Create views.py

`profile_api/views.py`

```python



```


### Creating Serializers

Serializer is a feature in django framework that allows you convert data inputs into python objects and vice-versa. Is similar to django forms when you define de inputs for your api.

Receive de content posted into the api.



```python

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name filed for testing our APIView"""
    

```

