from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import blogPost

# Create your views here.
def post_list(request):
	posts = blogPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
	return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
	post = get_object_or_404(blogPost, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})