from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Task)
class TaskTranslationOptions(TranslationOptions):
    fields = ('title_name', 'description')


