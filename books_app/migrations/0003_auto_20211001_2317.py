# Generated by Django 3.2.7 on 2021-10-01 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20211001_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(null=True, related_name='books_written', to='books_app.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(null=True, related_name='books', to='books_app.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ratings_count',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail',
            field=models.URLField(null=True),
        ),
    ]
