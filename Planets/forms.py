from django import forms

from .models import Planet

class PlanetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlanetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mb-4'

    class Meta:

        model = Planet
        fields=("__all__")