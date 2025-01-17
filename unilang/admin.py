from django.contrib import admin

from .models import Language, Word

admin.site.register(Language)
admin.site.register(Word)