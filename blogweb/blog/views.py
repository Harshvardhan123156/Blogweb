from django.shortcuts import render , HttpResponse
from blog.models import Post

def bloghome(request):
    allposts = Post.objects.all()
    context = { 'allposts' : allposts}
    return render(request , 'blog/bloghome.html' , context)

def blogpost(request , slug):
    post = Post.objects.filter(slug=slug).first()
    context = { 'post' : post }
    return render(request ,'blog/blogpost.html' , context)
# Create your views here.
