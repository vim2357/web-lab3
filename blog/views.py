from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # Create the post instance without saving it to the database yet
            post.author = request.user # Set the author field to the currently logged-in user
            post.save() # Now save the post to the database
            return redirect('post_detail', post_id=post.id) # Redirect to the post detail page after successful creation
    else:
        form = PostForm()  # If GET request, provide an empty form
    return render(request, 'blog/post_form.html', {'form': form})  # Render the form template for creating a new post



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.published.all()

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
