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
        self.fields['seed_pattern'].widget.attrs={
            'class': 'form-control me-auto border-success',
            'placeholder': 'Введите название продукции'
        }
        self.fields['type'].widget.attrs={
            'class': 'form-select border-success mb-3 mt-3',
        }


class Feedback(forms.Form):
    full_name = forms.CharField(max_length=200, label='Введите ФИО')
    phone_number = forms.CharField(max_length=100, label='Введите номер телефона')
    email = forms.EmailField(label='Введите почту')

    def __init__(self, *args, **kwargs):
        super(Feedback, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs={
            'class': 'form-control border-success mt-1 mb-3',
            'placeholder': 'Пупкин Василий Иванович'
        }
        self.fields['phone_number'].widget.attrs={
            'type': 'text',
            'class': 'form-control border-success bfh-phone mt-1 mb-3',
            'data-format': '+7 (ddd) ddd-dd-dd',
            'placeholder': '+7 (999) 999-99-99'
        }
        self.fields['email'].widget.attrs={
            'class': 'form-control border-success mt-1 mb-4',
            'placeholder': 'example@yandex.ru'
        }
