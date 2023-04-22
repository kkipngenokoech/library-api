from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTest(TestCase):
    @classmethod
    def SetUpTestData(cls):
        cls.book = Book.objects.create(
            title = 'The Lord of the Rings',
            subtitle = 'the lord of rings subtitles',
            author = 'J. R. R. Tolkien',
            isbn = '0-553-21311-3',
        )

    def testBookInstance(self):
        self.assertEqual(self.book.title, 'The Lord of the Rings')
        self.assertEqual(self.book.subtitle, 'the lord of rings subtitles')
        self.assertEqual(self.book.author, 'J. R. R. Tolkien')
        self.assertEqual(self.book.isbn, '0-553-21311-3')

    def testBookListView(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'lord of rings ')
        self.assertTemplateUsed(response, "books/book_list.html")