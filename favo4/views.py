from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import Content, Chara, Favorite4, PostTwi, CustomUser
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet
from .forms import ContentCreateForm, CharaFormset
from . import forms, twitter_api
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import os
import json
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "index.html"


class F4ListView(generic.ListView):
    template_name = "list.html"
    model = Content
    paginate_by = 10


def add_content(request):
    form = ContentCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        content = form.save(commit=False)
        formset = CharaFormset(request.POST, files=request.FILES, instance=content)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            content.user = request.user
            content.save()
            formset.save()
            return redirect('favo4:F4-list')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = CharaFormset()

    return render(request, 'create.html', context)


def f4_post_twi_view(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST' and request.user:
        selected_choice = request.POST.getlist('choice')
        user = request.user
        if len(selected_choice) == 0 or len(selected_choice) >= 5:
            return render(request, 'post-twi.html', {
                'content': content,
                'error_message': "未選択か、5つ以上選択しています",
            })
        favo4 = Favorite4.objects.create(user=user, content=content).pk
        box = []
        content_box = []
        image_box = []
        for i in selected_choice:
            f4 = PostTwi(user=user, chara=Chara.objects.get(pk=i),
                         favorite4=Favorite4.objects.get(pk=favo4))
            content_box.append(Chara.objects.get(pk=i).chara_name)

            image = Chara.objects.get(pk=i).photo
            with image.open() as imagefile:
                imagedata = imagefile.read()
            image_box.append(imagedata)
            box.append(f4)

        PostTwi.objects.bulk_create(box)

        twi_content = ','.join(content_box)
        twitter_res = twitter_api.post_twitter(user, twi_content, image_box)
        JsonResponse(twitter_res)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('favo4:F4-post-twi', args=(content.id,)))

    elif request.method == 'GET':
        return render(request, 'post-twi.html', {
                'content': content,
            })
    else:
        return redirect('https://google.com')


class F4UserPageView(generic.DeleteView):
    template_name = "user-page.html"
    model = Favorite4, PostTwi
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url = reverse_lazy('favo4:F4-user-page')

    def get_object(self):
        # slugからuserを取ってる？
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        # いずれにせよobjectを返し、表示するuserとログインユーザーを差別化している
        # if self.request.user.username == object.username:
        return object
        # else:
        #     print("you are not the owner!!")

    def get_context_data(self, **kwargs):
        # クエリセット　usernameと一致したオブジェクトを取得し、配列に返している
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        context = super().get_context_data(**kwargs)
        context.update({
            'object_list2': Favorite4.objects.filter(user=object).order_by('created_at').reverse(),
        })
        return context

    def delete(self, request, *args, **kwargs):
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        if request.user != object:
            return redirect('https://google.com')
        # チェックボックスに入った情報複数削除
        selected_choice = request.POST.getlist('del-choice')
        for i in selected_choice:
            Favorite4.objects.filter(pk=i).delete()
        return HttpResponseRedirect(reverse('favo4:F4-user-page', args=(request.user,)))
