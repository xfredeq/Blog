# Generated by Django 4.0.3 on 2022-03-22 22:32

import django.core.validators
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
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('excerpt', models.CharField(max_length=250)),
                ('image_name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(25)])),
                ('author', models.ForeignKey(default='Unknown', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
    ]
