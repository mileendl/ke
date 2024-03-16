from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('account/login', views.user_login, name='login'),
    path('account/register', views.register, name='register'),
    #path('list/lists', views.list_lists, name='list_lists'),
    #path('list/objs', views.list_objs, name='list_objs'),
    #path('list/create', views.create_list, name='create_list'),  
]