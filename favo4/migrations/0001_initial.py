# Generated by Django 3.1.7 on 2021-03-11 03:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=8, verbose_name='タイトル')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Chara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chara_name', models.CharField(max_length=10, verbose_name='キャラ名')),
                ('photo', models.ImageField(upload_to='', verbose_name='キャラ画像')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favo4.content', verbose_name='コンテンツ')),
            ],
            options={
                'verbose_name_plural': 'Chara',
            },
        ),
    ]