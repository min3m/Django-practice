from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') # order_by('-pk')로 역순 정렬! 'pk'이면 오름차순이겠지.

    return render(
        request,
        'blog/index.html',
        {
			'abc': posts,
		}
        )
