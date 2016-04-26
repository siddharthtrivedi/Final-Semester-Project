from django import template

register = template.Library()

@register.filter(name='addcss')

def addcss(field, arg):
	return field.as_widget(attrs={"class": arg})

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)