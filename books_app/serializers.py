from rest_framework import serializers

from books_app.models import Author, Category, Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Author.objects.all())
    categories = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ("id",
                  "title",
                  "authors",
                  "published_data",
                  "categories",
                  "average_rating",
                  "rating_count",
                  "thumbnail")
