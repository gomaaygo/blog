from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm


def post_list(request):
	posts = Post.objects.filter(publish_date__lte=timezone.now())
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form' : form})