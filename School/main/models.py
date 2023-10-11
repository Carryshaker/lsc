from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created_at']

class Testlesson(models.Model):
    phone_number = models.TextField(blank=True)
    name = models.TextField(blank=True)
    datetime = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Пробный урок'
        verbose_name_plural = 'Пробные уроки'