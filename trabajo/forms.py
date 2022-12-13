from django import forms
from trabajo.models import Familia
from trabajo.models import Ciudad

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)


class FamiliaForm(forms.ModelForm):
  class Meta:
    model = Familia
    fields = ['nombre', 'apellido_paterno', 'apellido_materno' , 'direccion', 'fecha_nacimiento', 'sexo', 'ciudad'] 
    

  
class CiudadForm(forms.ModelForm):  
  class Meta:
    model = Ciudad
    fields = ['nombre_ciudad', 'codigo_postal', 'provincia' ] 


 