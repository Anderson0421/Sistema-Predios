from django.forms import *

from erp.userauths.models import Deuda, Predio





class PredioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['placeholder'] = 'Introduzca su '+ form.label
        self.fields['propietario'].widget.attrs['class'] = 'form-control select2'

    class Meta:
        model = Predio
        fields = '__all__'



class DeudaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['contribuyente'].widget.attrs['class'] = 'form-control select2'

    class Meta:
        model = Deuda
        fields = '__all__'



