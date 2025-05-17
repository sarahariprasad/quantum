from django import template

register = template.Library()

@register.filter
def split_sentences(value):
    if not value:
        return []
    # Split by period, strip spaces, and remove empty strings
    sentences = [s.strip() for s in value.split('.') if s.strip()]
    return sentences



#### for job details page #####

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})

### ended job details page #############

