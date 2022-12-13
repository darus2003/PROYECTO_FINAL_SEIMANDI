from django.shortcuts import render
from trabajo.models import Familia
from trabajo.forms import Buscar # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT


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