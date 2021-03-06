from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import blogPost
from .forms import PostForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.
def post_list(request):
	posts = blogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(blogPost, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(blogPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'blog/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return post_list(request)
    else:
        return invalid_login(request)

def invalid_login(request):
    return render(request, 'blog/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'blog/post_list.html')