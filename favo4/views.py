from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from .models import Content, Chara, PostTwi
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet
from .forms import ContentCreateForm, CharaFormset
from . import forms
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
    try:
        choices = content.chara_set.get(pk=request.POST['choice'])
    except (KeyError, PostTwi.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'post-twi.html', {
            'content': content,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice = request.POST.getlist('choice')
        box = []
        for i in selected_choice:
            f4 = PostTwi(user=request.user, chara=Chara.objects.get(pk=i), content=content)
            box.append(f4)
        PostTwi.objects.bulk_create(box)

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('favo4:F4-post-twi', args=(content.id,)))

