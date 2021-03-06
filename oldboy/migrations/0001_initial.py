# Generated by Django 2.1.4 on 2019-01-07 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='图片名称')),
                ('img', models.FileField(upload_to='static/img', verbose_name='图片路径')),
                ('target', models.URLField(verbose_name='跳转路径')),
                ('status', models.IntegerField(choices=[(1, '上线'), (2, '下线')], verbose_name='状态')),
                ('weight', models.IntegerField(verbose_name='权重')),
            ],
        ),
    ]
