from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email)


class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=False)
    content = models.TextField(validators=[MinLengthValidator(25)])

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, default='Unknown')
    tags = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return "{} ({})".format(self.title, self.date)
