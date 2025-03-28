from django import template 
from transliterate import translit
  
register = template.Library() 


@register.filter() 
def transliter(value: str, lang: str) -> str:
    if lang == 'ru':
        return translit(value.replace('_', '\'').replace('-', ' '), 'ru').replace('Ь', 'ь')
    if lang == 'en':
        return translit(value, 'ru', reversed=True).replace('\'', '_').replace(' ', '-')
