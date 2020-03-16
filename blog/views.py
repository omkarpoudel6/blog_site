from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    queryset=Post.objects.filter(featured=True)
    object={'object':queryset}

    return render(request,'index.html',context=object)

def blog(request):
    return render(request,'blog.html')

def post(request):
    return render(request,'post.html')