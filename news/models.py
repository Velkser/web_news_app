from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата публикации")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=6)

    def __str__(self) -> str:
        return self.title
    
