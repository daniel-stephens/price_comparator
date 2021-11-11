from django import forms


class PhoneSearchForm(forms.Form):
    phone = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = ""
        self.fields['phone'].widget.attrs.update({
            "class": "form-control"
        })