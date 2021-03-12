from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from .models import Content, Chara, PostTwi
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet
from .forms import ContentCreateForm, CharaFormset, PostTwiForm
from . import forms
from django.template.context_processors import csrf
# Create your views here.


class HomeView(generic.TemplateView):
    template_name = "index.html"


class F4ListView(generic.ListView):
    template_name = "list.html"
    model = Content
    paginate_by = 10


class F4DetailView(generic.DetailView):
    template_name = "detail.html"
    model = Content


# class CharaInlineFormSet(InlineFormSet):
#     model = Chara
#     fields = ("chara_name", "photo")
#     # content = Content.objects.get(name=)
#     # add_charas = []  # 作成クエリの配列
#     # for i in range(5):
#     #     chara = Chara(chara_name=i, photo=i, content=content)
#     #     add_charas.append(chara)  # 作成クエリを配列に格納
#     #
#     # Chara.objects.bulk_create(add_charas)
#
#
# class F4CreateView(CreateWithInlinesView):
#     model = Content
#     fields = ("title",)
#     inlines = [CharaInlineFormSet, ]
#     template_name = "create.html"
#     success_url = reverse_lazy('favo4:F4-list')
#
#     def form_valid(self, form):
#         content = form.save(commit=False)
#         content.user = self.request.user
#         content.save()
#         messages.success(self.request, '作成しました。')
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         messages.error(self.request, "作成に失敗しました。")
#         return super().form_invalid(form)

def add_content(request):
    form = ContentCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        content = form.save(commit=False)
        formset = CharaFormset(request.POST, files=request.FILES, instance=content)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
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


# class F4PostTwiView(generic.CreateView):
#     model = PostTwi
#     template_name = "post-twi.html"


def f4_post_twi_view(request, pk):
    labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
    # 入力結果を格納する辞書
    results = {}
    ret = ''
    if request.method == 'POST':
        # 入力されたデータの受取
        results[labels[3]] = request.POST.getlist("four")
        ret = 'OK'
        c = {'results': results, 'ret': ret}
    else:
        form = forms.PostTwiForm()
        choice1 = []
        for i in range(3):
            choice1.append(('1', i))
        # choice1.append(('2', '動的選択肢２'))
        # choice1.append(('3', '動的選択肢３'))
        # choice1.append(('4', '動的選択肢４'))
        form.fields['four'].choices = choice1
        form.fields['four'].initial = ['2']
        c = {'form': form, 'ret': ret}
        # CFRF対策（必須）
        c.update(csrf(request))
    return render(request, 'post-twi.html', c)
