from django.db import models

# Create your models here.
class Post(models.Model):
    """
    포스트의 형태를 정의하는 Post 모델
    제목(title), 내용(content), 작성일(created_at), 작성자 정보(author)
    """
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField()

    def __str__(self):
        # 포스트 번호와 제목 보여주는 부분.
        # 장고에선 model이 만들어지면 만들어진 순서대로 고유의 pk값을 가짐.
        return f'[{self.pk}]{self.title}'

    # upload_to에 이미지를 저장할 폴더의 경로 규칙을 정해놓는것!
    # blank=True -> 해당필드는 필수가 아니다!
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now_add=True는 최초로 등록되었을 시에만 현재날짜를 적용
    # auto_add=True model이 save 될때마다 현재날짜로 갱신.

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    # author = 추후 작성될 모델, 외래키 구현시 다룸.
