from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.Home, name='home'),
    path('posts', views.post_list, name='posts'),
    path('gallery', views.gallery_view, name='image_gallery' ),
    path('vichar', views.thoughts_view, name='thoughts_page' ),
    path('<slug:slug>', views.post_detail , name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
    
]

