from django.urls import path
from django.conf.urls import url


from blog.views import  read_post, add_post, edit_post, view_test, get_posts_by_tag,   post_like, trial_artists



urlpatterns = [
    # path('posts/unpublished', get_unpublished_posts, name = 'get_unpublished_posts'),
    path("posts/<int:id>/read", read_post, name = 'read_post'),
    path('posts/<int:id>/edit', edit_post, name='edit_post'),
    path('posts/add', add_post, name='add_post'),
    # path('posts/<int:id>/publish', publish_post, name='publish_post'),
    
    path('blog/test-posts.html', view_test, name = 'view_test'),
    path('tag/<tag>', get_posts_by_tag, name='posts_by_tag'),
    
    path('posts/<int:id>/read/like', post_like, name='post_like'),
    path('blog/trial_artists.html', trial_artists, name = 'trial_artists'),
    
    
    
         
  
    ]
