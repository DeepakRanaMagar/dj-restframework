from django.test import TestCase
from django.urls import reverse

from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title= 'A Great Book Title',
            subtitle= 'A Great Book Subtitle',
            author= 'A Great Book Author',
            isbn= '1234567890123',
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, 'A Great Book Title')
        self.assertEqual(self.book.subtitle, 'A Great Book Subtitle')
        self.assertEqual(self.book.author, 'A Great Book Author')
        self.assertEqual(self.book.isbn, '1234567890123')
        
    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A Great Book Title')
        self.assertTemplateUsed(response, 'books/book_list.html')