# Generated by Django 2.2.2 on 2019-12-30 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20191218_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeroClassify',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序列号')),
                ('name', models.CharField(max_length=5, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='HeroList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序列号')),
                ('name', models.CharField(max_length=10, verbose_name='英雄名')),
                ('classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.HeroClassify')),
            ],
        ),
    ]