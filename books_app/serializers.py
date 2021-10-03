from rest_framework import serializers

from books_app.models import Author, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    # authors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Author.objects.all())
    # categories = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Category.objects.all())
    authors = AuthorSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = ("id",
                  "title",
                  "authors",
                  "published_date",
                  "categories",
                  "average_rating",
                  "ratings_count",
                  "thumbnail")

    def create(self, validated_data):
        authors = validated_data.pop("authors", None)
        categories = validated_data.pop("categories", None)

        book, created = Book.objects.get_or_create(**validated_data)
        if book:
            for author in authors:
                author, created = Author.objects.get_or_create(name=author['name'])
                book.authors.add(author)
            for category in categories:
                category, created = Category.objects.get_or_create(name=category['name'])
                book.categories.add(category)
        book.save()
        return book
