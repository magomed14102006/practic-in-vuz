from django.db import models


class Articles(models.Model):
    name = models.CharField('Имя', max_length=100)
    anons = models.CharField('Анонс', max_length=200)
    text = models.TextField('Текст', max_length=50000)
    data = models.DateField('Дата публикации')

    def __str__(self):
        return self.name