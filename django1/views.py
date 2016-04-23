from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


def info(request):
	return render(request, 'info.html', {'posts': Post.objects.all()})