from django.db import models


class Book(models.Model):
    """書籍"""
    book_no = models.IntegerField('書籍番号', primary_key=True)
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255)
    category = models.CharField('カテゴリ', max_length=255)

    def __str__(self):
        return self.name

