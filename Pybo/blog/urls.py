from django.urls import path
from . import views # 현재 폴더에 있는 views.py를 사용하겠다는 뜻

urlpatterns = [
    path('', views.index)
]
