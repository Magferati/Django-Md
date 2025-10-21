from django import forms
from .models import Daisy

class DaisyForm(forms.ModelForm):
    class Meta:
        model = Daisy
        fields = "__all__"