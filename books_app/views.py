from django.shortcuts import render
from rest_framework import generics

from books_app.models import Book
from books_app.serializers import BookSerializer


class BooksListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
