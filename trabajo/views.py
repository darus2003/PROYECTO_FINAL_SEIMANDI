from django.shortcuts import render
from trabajo.models import Familia
from trabajo.forms import Buscar, FamiliaForm, CiudadForm
from django.views import View


# Create your views here.
def index(request):
    return render(request, "trabajo/saludar.html")

def monstrar_familia(request):
  lista_familiares = Familia.objects.all()
  return render(request, "trabajo/familia.html", {"lista_familiares": lista_familiares})


class BuscarFamilia(View):
    form_class = Buscar
    template_name = 'trabajo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familia.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamilia(View):

    form_class = FamiliaForm
    template_name = 'trabajo/alta_familia.html'
    initial = {'nombre':'', 
                'apellido_paterno':'', 
                'apellido_materno':'' , 'direccion':'', 'fecha_nacimiento':'', 'sexo':'', 'ciudad':''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"ALTA CON EXITO {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class AltaCiudad(View):

    form_class = CiudadForm
    template_name = 'trabajo/alta_ciudad.html'
    initial = {'nombre_ciudad':'', 'codigo_postal':'', 'provincia':"" }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"ALTA CON EXITO {form.cleaned_data.get('nombre_ciudad')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})