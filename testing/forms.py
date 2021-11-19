from django.db.models import fields
from django.forms.models import ModelForm, modelform_factory
from .models import post

class postform(ModelForm):
    class Meta:
        model = post
        fields = "__all__"