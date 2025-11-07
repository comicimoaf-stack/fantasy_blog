from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Mostrar últimos posts primero
    return render(request, 'home.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})

