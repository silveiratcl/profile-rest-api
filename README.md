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

### Creating Serializers

Serializer is a feature in django framework that allows you convert data inputs into python objects and vice-versa. Is similar to django forms when you define de inputs for your api.

Receive de content posted into the api.


## APIView and ViewSet

### Api Views

1. APIview
Describes the logic to make API endpoint.

APIviews allows to use the standar HTTP methods for functions.
+ get - return one or more itens
+ post - create an item
+ put - update an item
+ patch - partially update an item

APIviews give the most control over the logic:
+ perfect for implementing complex logic
+ Calling other APIs
+ Working with local files

When to use APIviews:
+ Needs full control over the logic
+ Processing file and rendering a sychronous response
+ You are calling other APIs/services
+ Acessing local files or data

### Create the first API View

Create views.py

`profile_api/views.py`

```python

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializer a name filed for testing our APIView"""
    

```

### Viewset 

Just like API Views, ViewSets allow us write the logic for our endpoints, however instead of definig functions which map to HTTP view sets accept functions that map to common API objects actions:

Uses model operation for function:
+ list - getting a lis of objects
+ create - create ne objects
+ retrive - getting anm specific object
+ update - update object
+ partial_update - updating part of an object
+ destroy - deleting an object

Additionaly, ViewSets can take:
+ a lot of the common logic 
+ Perfect for standard database operations
+ Fastest way to make databases interfaces

When to use:

+ Could be used into simple CRUD interface to your database
+ A quick and simple API
+ Little to no customization on the logic 


## Planning Profiles API

The app will have the following options:

1. Create a new profile
+ Handle registration of new users
+ Validate profile data

2. Listing existing profiles
+ Search for profiles
+ Email and name

3. View sopacific profiles
+ Profile ID

4. Update profile of logged in user
+ Change name, email and password

5. Delete profile

### API URLS

`/api/profile/` 
+ list all profiles when *HTTP GET* method is called
+ create new profile when *HTTP POST* method is called

`/api/profile/<profile>`
+ view specific profile details by using *HTTP GET*
+ update object using *HTTP PUT/PATCH*
+ remove it completely using *HTTP DELETE*









