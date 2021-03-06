# Generated by Django 3.2.7 on 2021-10-01 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_date', models.SmallIntegerField()),
                ('average_rating', models.SmallIntegerField()),
                ('ratings_count', models.SmallIntegerField()),
                ('thumbnail', models.URLField()),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_written', to='books_app.author')),
                ('categories', models.ManyToManyField(related_name='books', to='books_app.Category')),
            ],
        ),
    ]
