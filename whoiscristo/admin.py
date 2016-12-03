from django.contrib import admin

from .models import CristoPoll, Vote, Choice

admin.site.register(CristoPoll)
admin.site.register(Vote)
admin.site.register(Choice)