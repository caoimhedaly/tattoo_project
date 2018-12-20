from django.urls import path
from django.conf.urls import url


from blog.views import  read_post, add_post, edit_post, publish_post, get_unpublished_posts, get_all_posts, view_test, get_posts_by_tag, get_all_artists,  post_like, trial_artists



urlpatterns = [
    path('posts/unpublished', get_unpublished_posts, name = 'get_unpublished_posts'),
    path("posts/<int:id>/read", read_post, name = 'read_post'),
    path('posts/<int:id>/edit', edit_post, name='edit_post'),
    path('posts/add', add_post, name='add_post'),
    path('posts/<int:id>/publish', publish_post, name='publish_post'),
    path('blog/all_posts.html', get_all_posts, name = 'get_all_posts'),
    path('blog/test-posts.html', view_test, name = 'view_test'),
    path('tag/<tag>', get_posts_by_tag, name='posts_by_tag'),
    path('blog/all_artists.html', get_all_artists, name = 'get_all_artists'),
    path('posts/<int:id>/read/like', post_like, name='post_like'),
    path('blog/trial_artists.html', trial_artists, name = 'trial_artists'),
    
    
    
         
  
    ]