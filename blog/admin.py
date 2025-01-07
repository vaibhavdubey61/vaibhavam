from django.contrib import admin
from .models import Post , Category, GalleryImage, Thought

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(GalleryImage)
admin.site.register(Thought)

