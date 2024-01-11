from django import forms
from testapp.models import product_details,Bills

class product(forms.ModelForm):
    class Meta:
        model = product_details
        fields = "__all__"

class product_bills(forms.ModelForm):
    class Meta:
        model = Bills
        fields = "__all__"
