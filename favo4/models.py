from accounts.models import CustomUser
from django.db import models

# Create your models here.


class Content(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=8)
    user = models.ForeignKey(CustomUser, verbose_name="ユーザー", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Content'

    def __str__(self):
        return self.title


class Chara(models.Model):
    chara_name = models.CharField(verbose_name='キャラ名', max_length=10)
    photo = models.ImageField(verbose_name='キャラ画像')
    content = models.ForeignKey(Content, verbose_name='コンテンツ', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Chara'

    def __str__(self):
        return self.chara_name


class Favorite4(models.Model):
    content = models.ForeignKey(Content, verbose_name='コンテンツ', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Favorite4'

    def __str__(self):
        return self.content.title + ', ' + self.user.username


class PostTwi(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    chara = models.ForeignKey(Chara, verbose_name='キャラ', on_delete=models.CASCADE)
    favorite4 = models.ForeignKey(Favorite4, verbose_name='F4', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'PostTwi'

    def __str__(self):
        return self.chara.chara_name
