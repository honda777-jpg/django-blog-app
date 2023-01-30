from django.db import models

# Create your models here.
class Post(models.Model): #これから作成するPostクラスが、Djangoで使用するmodelであることを定義
    #項目定義
    title = models.CharField(max_length=100) #titleという名前の最大100文字まで入る文字列のカラム作成
    content = models.TextField() #TextFieldも文字列を扱えるが、最大数を記載する必要はなし。CharFeildは指定必須
    create_at = models.DateTimeField(auto_now_add=True) #DateTimeFeildは日時を扱える。auto_now_add=Trueにすることで、新規作成時自動で日付が入る
    updated_at = models.DateTimeField(auto_now=True) #auto_now=Trueにすることで、更新時自動で日付が入る

    #テキスト表示
    def __str__(self):
        return self.title


