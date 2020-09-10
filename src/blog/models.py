from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntegerField()

    # 제목 보여주기, view_count 보여주기
    def __str__(self):
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 100)
