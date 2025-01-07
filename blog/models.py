from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.html import strip_tags

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True,blank=True, max_length=100)
    
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.title
    
    '''def snippet(self):
        return self.body[:150] + '...' '''
    
    def snippet(self):
    # Strip HTML tags using Django's built-in function
        plain_text = strip_tags(self.body)
        if len(plain_text) > 150:
            return plain_text[:150] + '...'
        return plain_text
    
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.TextField()

    def __str__(self):
        return self.caption

class Thought(models.Model):
    thought = models.TextField()

    def __str__(self):
        return self.thought[:50]    
    