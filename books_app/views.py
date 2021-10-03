import requests
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from books_app.models import Book, Author, Category
from books_app.serializers import BookSerializer, AuthorSerializer, CategorySerializer


class BooksListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        published_date = self.request.query_params.get('published_date', None)
        author = self.request.query_params.get('author', None)
        sort = self.request.query_params.get('sort', None)
        if published_date is not None:
            queryset = queryset.filter(published_date__contains=published_date)
        if author is not None:
            queryset = queryset.filter(authors__name=author)
        if sort is not None:
            queryset = queryset.order_by(sort)
        return queryset


class BookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UploadBooksView(APIView):
    def get_items(self):
        res = requests.get("https://www.googleapis.com/books/v1/volumes", params={'q': 'war'})
        if res.status_code == 200:
            data = res.json()
            return data['items']
        else:
            return Response({'error': "Request failed"}, status=res.status_code)

    def post(self, request):
        data = self.get_items()
        for book in data:
            info = book['volumeInfo']
            serializer = BookSerializer(data={
                'title': info.get('title', None),
                'authors': [{'name': author} for author in info.get('authors', [])],
                'published_date': info.get('publishedDate', None),
                'categories': [{'name': category} for category in info.get('categories', [])],
                'average_rating': info.get('averageRating', None),
                'ratings_count': info.get('ratingsCount', None),
                'thumbnail': info['imageLinks'].get('thumbnail'),
            })
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response('Created successfully', status=status.HTTP_201_CREATED)
