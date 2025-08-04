from django.shortcuts import render , HttpResponse
from blog.models import Post

def bloghome(request):
    allposts = Post.objects.all()
    context = { 'allposts' : allposts}
    return render(request , 'blog/bloghome.html' , context)
# Create your views here.
