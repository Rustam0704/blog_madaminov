from django.contrib import admin

from madaminov.models import About, Author, Post


# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )

