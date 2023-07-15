#-*- coding:utf-8 -*-
from .models import User_Request
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = User_Request
        fields = "__all__"
