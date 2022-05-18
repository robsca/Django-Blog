from django.urls import path
from .views import post_detail, all_post, home

urlpatterns = [
    path('all_post/', all_post, name='all_post'),
    path('post_detail/<int:auto_increment_id>/', post_detail, name='post_detail'),
    path('', home, name='home'),
]