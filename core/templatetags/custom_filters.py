from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def auth_messages(messages):
    auth_tags = ['login', 'signup', 'password_reset', 'password_change']
    return [message for message in messages if message.extra_tags in auth_tags]