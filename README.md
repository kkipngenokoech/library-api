# library-api

here i will build out a basic Library website with traditional Django and then extend it into a web API with Django REST Framework.

## prerequiste

one has to build the traditional django application first with the MVT, and as for now we hava already built the library MVT

## library api

Our Library website currently consists of a single page that displays all books in the database. To
transform it into a web API we will install Django REST Framework and create a new URL that
acts an API endpoint outputting all available books

a web API does not output a traditional webpage with HTML, CSS, and JavaScript. Instead, it is just pure data
( often in the JSON format) and accompanying HTTP verbs that specify what user actions are
allowed. In this instance, an API user can only read the content, they are not able to update it in
any way though we will learn how to do that in future chapters.

## django rest framework

pip3 install djangorestframework -  this will install the rest framework and dont forget to list this app in your settings so as to inform our django application of the third party framework.

Ultimately, our web API will expose a single endpoint that lists out all books in JSON. To do this,
we will need a new URL route, a new view, and a new serializer file

## [apis](./apis/)

this application we have created just for the purpose of creating apis, and so we wont be using the app's models since we wont be creating any new data.

In traditional Django views are used to customize what data to send to the templates. Django
REST Framework views are similar except the end result is serialized data in JSON format, not
the content for a web page! Django REST Framework views rely on a model, a URL, and a new
file called a serializer

## serializers

A serializer33 translates complex data like querysets and model instances into a format that is
easy to consume over the internet, typically JSON. It is also possible to “deserialize” data - the same process in reverse, whereby JSON data is first validated and then transformed into a
dictionary.

A serializer is a software component or library that converts data from one format to another, typically for the purpose of transmitting or storing that data. Serializers are commonly used in web development, where data is often transmitted between client and server in JSON or XML formats, but may need to be converted to other formats such as HTML or CSV for display or storage.

The process of serialization involves taking structured data, such as a Python dictionary or a Java object, and converting it into a serialized format, such as a JSON string or a binary message. This process can be reversed using a deserializer, which converts the serialized data back into its original format.

Some common serializers used in web development include the Django Rest Framework serializer, the Java Jackson serializer, and the Ruby on Rails ActiveModel serializer.

### django rest framework serializer

Django Rest Framework (DRF) is a powerful toolkit for building APIs using the Django web framework. DRF provides a serializer class that allows you to easily convert complex data types, such as Django models, into Python datatypes, and then into JSON or other content types.

Serializers define the fields that should be included in the output, and provide a mapping between the field names and their corresponding attributes on the model. Serializers also handle the conversion of incoming data from JSON back into Python objects.

To use a serializer in DRF, you define a serializer class that inherits from one of the built-in serializer classes, such as serializers.ModelSerializer or serializers.Serializer. You then define the fields that should be included in the output, and any additional options or validation rules that are needed.

### serializer class 101

you create the normal urls, models and views as you would for a traditional django application.

in the app level directory create a serializer module where you will define your serialized model

then in your views you: `serializer_class = model you want to serialize`
