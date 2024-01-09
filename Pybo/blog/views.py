from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') # order_by('-pk')로 역순 정렬! 'pk'이면 오름차순이겠지.

    return render(
        request,
        'blog/post_list.html',
        {
			'posts': posts,
		}
        )
def single_post_page(request, pk):
    post = Post.objects.get(pk = pk) # 매개변수로 받은 pk값과 같은 pk를 가져오라는 뜻!

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
        }
    )
