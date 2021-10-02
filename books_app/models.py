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
    title = models.CharField(max_length=255, null=True)
    authors = models.ManyToManyField(Author, related_name="books_written")
    published_date = models.CharField(max_length=12, null=True)
    categories = models.ManyToManyField(Category, related_name="books")
    average_rating = models.SmallIntegerField(null=True)
    ratings_count = models.SmallIntegerField(null=True)
    thumbnail = models.URLField(null=True)

    def __str__(self):
        return self.title
