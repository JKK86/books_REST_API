from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books_written")
    published_date = models.SmallIntegerField()
    categories = models.ManyToManyField(Category, related_name="books")
    average_rating = models.SmallIntegerField()
    ratings_count = models.SmallIntegerField()
    thumbnail = models.URLField()

    def __str__(self):
        return self.title
