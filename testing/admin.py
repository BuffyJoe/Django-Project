from django.contrib import admin
from .models import comments, finance, people, topic, post
# Register your models here.

admin.site.register(people)

admin.site.register(topic)
admin.site.register(post)
admin.site.register(finance)
admin.site.register(comments)