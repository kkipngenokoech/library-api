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

    