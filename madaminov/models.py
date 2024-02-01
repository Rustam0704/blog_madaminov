from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(AbstractUser):
    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]

    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class About(BaseModel):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return f" {self.title} "


class Post(BaseModel):
    title = models.CharField(max_length=40)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        verbose_name = 'Post'

    def get_absolute_url(self):
        return f"/post/{self.title}/"