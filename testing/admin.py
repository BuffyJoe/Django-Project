from django.contrib import admin
from .models import Like, comments, topic, post
# Register your models here.

admin.site.register(Like)
admin.site.register(topic)
admin.site.register(post)
admin.site.register(comments)