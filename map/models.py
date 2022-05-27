from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

class Map_Comment_Nokids(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() # 댓글 넣을 부분
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}' # 댓글 작성 사람과 댓글 내용 함께 출력하는 함수

    def get_absolute_url(self):
        return f'{self.get_absolute_url()}#comment-{self.pk}' # #부분이 id를 의미한 id를 누르면 absolute_url로 이동한다.

class Map_Review(models.Model):
    title = models.CharField(max_length=30) # 문자열 필드 , 맥시멈 30자까지
    hook_text = models.CharField(max_length=100, blank=True) # Blank Ture: 비워놔도 괜찮다 # hoot_text 흥미를 끌만한 내용들 미리보기
    content = models.TextField() # 긴 문장 쓸 수 있는 필드

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to ='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # author/category 다대일 관계로 설정
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #on_delete : 포스트 작성자가 DB에서 삭제되면 글도 같이 삭제, set_null : 작성자가 사라지면 작성자가 None으로 표시되게 설정

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}' # 앞에는 몇번째꺼인지 뒤에꺼는 제목을 넣는것 #기본키 pk(순서 표현때 자주 씀) #self는 자신 post의 타이틀

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

class Map_Comment_Playground(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField() # 댓글 넣을 부분
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}' # 댓글 작성 사람과 댓글 내용 함께 출력하는 함수
