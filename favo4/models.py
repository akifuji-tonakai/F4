from accounts.models import CustomUser
from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=15)
    copyright = models.CharField(verbose_name='権利表記', default='©︎', max_length=100)
    hashtag = models.CharField(verbose_name='ハッシュタグ', default='#Favorite4', max_length=20)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'コンテンツ'

    def __str__(self):
        return self.title


class Subclass(models.Model):
    sub_name = models.CharField(verbose_name='サブクラス', max_length=25)
    sub_image = models.ImageField(verbose_name='サブクラス画像', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'サブクラス'

    def __str__(self):
        return self.sub_name


class Chara(models.Model):
    chara_name = models.CharField(verbose_name='キャラ名', max_length=10)
    photo = models.ImageField(verbose_name='キャラ画像')
    content = models.ForeignKey(Content, verbose_name='コンテンツ', on_delete=models.CASCADE)
    subclass = models.ForeignKey(Subclass, verbose_name='サブクラス', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'キャラ'

    def __str__(self):
        return self.chara_name


class Favorite4(models.Model):
    content = models.ForeignKey(Content, verbose_name='コンテンツ', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Favorite4'

    def __str__(self):
        return self.content.title + ', ' + self.user.username


class PostTwi(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    chara = models.ForeignKey(Chara, verbose_name='キャラ', on_delete=models.CASCADE)
    favorite4 = models.ForeignKey(Favorite4, verbose_name='F4', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'マイページ'

    def __str__(self):
        return self.chara.chara_name
