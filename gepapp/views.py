from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from gepapp.models import paciente




# Create your views here.
def inserta_paciente(request):
    pac = paciente(nombre = 'Leandro',apellido = 'Rodriguez' , docuemnto = '30172062' , telefono = '1161460021', fecha_nacimiento = '1983-04-29',sexo = 'M', pais = 'Argentina')
    pac.save()
    ver_paciente_nuevo = f"Se Registro correctamente al pacinte:<br>Nombre: {pac.nombre} {pac.apellido} <br>Documento: {pac.docuemnto}<br>Telefono: {pac.telefono}<br>Pais: {pac.pais}"
    return HttpResponse(ver_paciente_nuevo)

def ver_pacientes(request):
    paci = paciente.objects.all()
    context = {'pacientes': paci}
    return render(request, 'C:/py/green/pacientes/appaciente/templates/pacientes.html', context)

def ver_cliente(request, cliente_id):
    cliente = paciente.objects.get(pk=cliente_id)
    return render(request, 'ver_cliente.html', {'cliente': cliente})