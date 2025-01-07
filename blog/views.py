from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import *


def post_list(request):
    posts= Post.objects.all()
   
    return render(request, 'bloglist.html', {'posts': posts})


def post_detail(request, slug):
    post=get_object_or_404(Post, slug=slug)
    data={
        'post': post
    }
    return render(request, 'blog_detail.html', data)

def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category).order_by('-created_date')
    return render(request, 'category_posts.html', {
        'category': category,
        'posts': posts
    })
    
def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def thoughts_view(request):
    thoughts = Thought.objects.all()
    return render(request, 'thoughts.html', {'thoughts': thoughts})
    


def Home(request):
    
    return render(request, 'landing.html')