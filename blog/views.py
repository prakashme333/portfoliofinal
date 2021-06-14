from django.shortcuts import render, get_object_or_404
from blog.models import blog

# Create your views here.
def forblog(request):
   post= blog.objects.all()
   return render(request, 'blog.html',{'post':post})

def detail(request,id):
   blog_post = get_object_or_404(blog,pk=id)
   return render(request, 'detail.html',{'post':blog_post})