from django.db import models


# Create your models here.
class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)


class Article(BaseModel):
    title = models.CharField(max_length=255)


class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # @classmethod
    # def do_like(cls, user_id: int, article_id: int) -> "Like":
    #     return cls.objects.create(user_id=user_id, article_id=article_id)
