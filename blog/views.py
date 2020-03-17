from django.shortcuts import render
from .models import Post,Signup

# Create your views here.
def index(request):
    featured=Post.objects.filter(featured=True)[0:3]
    latest=Post.objects.order_by('-timestamp')[0:3]
    if request.method=='POST':
        email=request.POST['email']
        new_signup=Signup()
        new_signup.email=email
        new_signup.save()
    context={
        'object':featured,
        'latest':latest
         }

    return render(request,'index.html',context)

def blog(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    context={
        'latest':latest
    }
    return render(request,'blog.html',context)

def post(request):
    return render(request,'post.html')