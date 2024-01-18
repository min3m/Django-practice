from django.urls import path
from . import views # 현재 폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view())
    # path('', views.index), FBV
    # path('<int:pk>/', views.single_post_page), FBV
]
