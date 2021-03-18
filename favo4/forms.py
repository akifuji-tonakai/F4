from django import forms
from .models import Content, Chara


class ContentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Content
        fields = 'title',
        # fields = '__all__' ↑userをテンプレート排除してます


CharaFormset = forms.inlineformset_factory(
    Content, Chara, fields='__all__',
    extra=10, max_num=100, can_delete=False
)