from django.db.models import fields
from django.forms.models import ModelForm, modelform_factory
from .models import post, comments

class postform(ModelForm):
    class Meta:
        model = post
        fields = ['Topic', 'post']

class commentform(ModelForm):
    class Meta:
        model = comments
        fields = ['comment']