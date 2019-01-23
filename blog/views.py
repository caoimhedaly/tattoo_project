from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from accounts.models import Artist
from reviews.forms import ReviewForm, CommentForm
from django.views.generic import RedirectView

# Create your views here.

def get_posts_by_tag(request, tag):
    posts = Post.objects.filter(tags__icontains=tag)
    return render(request, "blog/test-posts.html", {'posts': posts})


def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
    



def user_can_edit_post(request, post):
    wrote_the_post = post.author == request.user
    is_editor = is_in_group(request.user, 'editors')
    superuser = request.user.is_superuser
    return wrote_the_post or superuser or is_editor

    

def get_all_posts(request):
    
    posts = Post.objects.filter(published_date__lte = timezone.now())
    return render( request, "blog/all_posts.html", {'posts': posts})
    

    
def read_post(request, id):
      post = get_object_or_404(Post, pk=id)
      post.views += 1
      post.save()
     
    #   increments number of views
    
   
      can_edit = user_can_edit_post(request, post)
      can_publish = is_in_group(request.user, 'publisher')
     
      
      #only author/superuser/editor can edit blog
      #only publisher can publish
      
      return render(request, "blog/read_post.html", {'post': post, 'can_edit': can_edit, 'can_publish':can_publish})
      
@login_required     
def add_post(request):
    
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        post=form.save(commit=False)
        # dont save to database
        post.author = request.user
        # author= logged in user
        post.save()
        # finally save to database
        return redirect(read_post, post.id)
    else:    
        form = PostForm()
        return render(request, "blog/form.html", {'form': form })


  
def edit_post(request, id):
    
    post = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        return redirect(read_post, post.id)
    else:        
        form=PostForm(instance=post)
        return render(request, "blog/form.html", {'form': form })
 

@permission_required('blog.can_publish')
def get_unpublished_posts(request):
    posts = Post.objects.filter(published_date__gte = timezone.now())
    return render(request, "blog/index.html", {'posts': posts})    
    
@permission_required('blog.can_publish')
def publish_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.published_date = timezone.now()
    post.save()
    return redirect(read_post, post.id)
     
def view_test(request):

    
    posts = Post.objects.filter(published_date__lte = timezone.now())
    return render( request, "blog/test-posts.html", {'posts': posts})


def make_comment(request, id):
    post = get_object_or_404(Post, pk=id)
   
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment=form.save(commit=False)
        # dont save to database
        comment.author = request.user
        comment.post_id=id
        # author= logged in user
        comment.save()
        # finally save to database
        return redirect(read_post, id=id)
     
    else:
     
        form = CommentForm()
        return render(request, 'reviews/form.html', {'form':form})
        

    
@login_required 
def post_like(request, id):
        
        
      post = get_object_or_404(Post, pk=id)
        
      user = request.user
      
      if user in post.likes.all():
            post.likes.remove(user)
      else:
        post.likes.add(user)
       
      return render(request, "blog/read_post.html", {'post': post}) 


    
def trial_artists(request):
    
    artists = Artist.objects.all()
    return render( request, "blog/trial_artists.html", {'artists': artists})
    
    
    
  

