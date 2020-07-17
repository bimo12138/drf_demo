from django.db import models


class Base(models.Model):

    language = models.CharField(max_length=20, verbose_name="语言名")
    author = models.CharField(max_length=30, verbose_name="作者")
    create_time = models.DateField(verbose_name="发布时间")


class HeroClassify(models.Model):
    id = models.AutoField(verbose_name="序列号", primary_key=True)
    name = models.CharField(max_length=5, verbose_name="分类")

    def __str__(self):
        return self.name


class HeroList(models.Model):

    id = models.AutoField(verbose_name="序列号", primary_key=True)
    name = models.CharField(max_length=10, verbose_name="英雄名")
    classify = models.ForeignKey(HeroClassify, on_delete=models.CASCADE)
