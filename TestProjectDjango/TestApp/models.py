from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class News(models.Model):
    photo = models.ImageField(upload_to='images', verbose_name='Фото', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    ctreate_at = models.DateTimeField(auto_now=True, verbose_name="Время публикации")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория новости")
    autor = models.CharField(max_length=255, verbose_name="Автор", blank=True, default=None, null=True, )
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
