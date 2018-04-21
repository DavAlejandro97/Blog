from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here. Va

def listadoPosts(request):
    posts = Post.objects.filter(fechaCreacion__lte = timezone.now()).order_by('fechaPublicacion')
    return render(request,'cuerpo2/listadoPosts.html',{'posts':posts})


