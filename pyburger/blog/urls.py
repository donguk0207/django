from django.urls import path, include
from config.views import index, burger_list, burger_search
from blog.views import post_list

urlpatterns = [
    path("", blog_index),
    path("posts/", include('blog.urls')),
]
