from django.contrib import admin
from .models import Author,Category,Post,Signup

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Signup)