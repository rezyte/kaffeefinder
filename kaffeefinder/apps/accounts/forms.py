from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class CafeManagerCreationForm(UserCreationForm):
    
    def save(self, commit=True):
        usr = super(CafeManagerCreationForm, self).save(commit=False)
        mnger_gp, created = Group.objects.get_or_create(name="cafe manager") 
        mnger_gp.user_set.add(usr)
        return usr

