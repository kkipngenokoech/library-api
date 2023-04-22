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

