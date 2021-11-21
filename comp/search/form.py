from django import forms




class PhoneSearchForm(forms.Form):
    phone = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].label = "SEARCH"
        self.fields['phone'].widget.attrs.update({
            "class": "form-control"
        })



condition =[('Used','Used'),
         ('New','New')]

regions = [ ('Ahafo', 'Ahafo'),
            ('Ashanti', 'Ashanti'),
            ('Bono', 'Bono'),
            ('Bono East', 'Bono East'),
            ('Central', 'Central'),
            ('Eastern', 'Eastern'),
            ('Oti', 'Oti'),
            ('Greater Accra', 'Greater Accra'),
            ('Northern', 'Northern'),
            ('North East', 'North East'),
            ('Savanna', 'Savanna'),
            ('Upper East', 'Upper East'),
            ('Upper West', 'Upper West'),
            ('Volta', 'Volta'),
            ('Western', 'Western'),
            ('Western North', 'Western North')]


class ConditionForm(forms.Form):
    conditions = forms.ChoiceField(choices=condition, widget=forms.RadioSelect(attrs={'onchange': 'submit();'}))

class RegionForm(forms.Form):
    regions = forms.ChoiceField(choices=regions, widget=forms.RadioSelect())