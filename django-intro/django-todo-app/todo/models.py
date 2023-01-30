from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField("タイトル", max_length=30) # 最大文字列30文字
    description = models.TextField("説明", blank=True) # TextFieldも文字列を扱える。blank=Trueでnull許容
    deadline = models.DateField("締切日") # 日付を扱える

    def __str__(self):
        return self.title
