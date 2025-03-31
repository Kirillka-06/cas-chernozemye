from django import forms
from .models import Seed, Type

class Search(forms.Form):
    seed_pattern = forms.CharField(max_length=100, required=False)
    type = forms.ChoiceField(
        choices=(('', ''),) + tuple((obj.translit, obj.name) for obj in Type.objects.all()),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(Search, self).__init__(*args, **kwargs)
        self.fields['seed_pattern'].widget.attrs={'class': 'form-control me-auto border-success'}
        self.fields['type'].widget.attrs={'class': 'form-select border-success mb-3 mt-3'}


class Feedback(forms.Form):
    full_name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=100)
    email = forms.EmailField()
