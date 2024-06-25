from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Post,Profile,UserMessage
from .forms import PostForm,UserRegistrationForm,MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
import os

def post_list(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(user__username__icontains=query).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'post_list.html', context)

@login_required
def download_file(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    file_path = post.file.path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/octet-stream")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("File not found")

@login_required
def post_generate(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            Profile.objects.create(user=user, image=request.FILES.get('prophoto', 'default.jpg'))
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('post_list')
    else:
        form = MessageForm()
    return render(request, 'compose_message.html', {'form': form})

@login_required
def inbox(request):
    received_messages = UserMessage.objects.filter(receiver=request.user)
    return render(request, 'inbox.html', {'received_messages': received_messages})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(UserMessage, id=message_id, receiver=request.user)
    if request.method == "POST":
        message.delete()
        return redirect('inbox')
    return redirect('inbox')

@login_required
def profile_dashboard(request):
    user = request.user
    return render(request, 'profile_dashboard.html', {'user': user})

@login_required
def user_dashboard(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(user=user).order_by('-created_at')
    user_profile = user.profile

    context = {
        'user': user,
        'user_posts': user_posts,
        'user_profile': user_profile
    }
    return render(request, 'user_dashboard.html', context)