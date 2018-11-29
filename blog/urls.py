from django.urls import path


from blog.views import  read_post, add_post, edit_post, publish_post, get_unpublished_posts



urlpatterns = [
    path('posts/unpublished', get_unpublished_posts, name = 'get_unpublished_posts'),
    path("posts/<int:id>/read", read_post, name = 'read_post'),
    path('posts/<int:id>/edit', edit_post, name='edit_post'),
    path('posts/add', add_post, name='add_post'),
    path('posts/<int:id>/publish', publish_post, name='publish_post'),
   
  
    ]