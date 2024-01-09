from django.shortcuts import render

# Create your views here.

#대문 페이지 랜더링 해주는 부분
def landing(request):
    return render(
		request,
		'single_pages/landing.html'
	)

#about me 페이지 랜더링 해주는 부분
def about_me(request):
    return render(
		request,
		'single_pages/about_me.html'
	)
