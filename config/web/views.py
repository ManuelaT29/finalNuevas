from django.shortcuts import render
from django.shortcuts import redirect


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.formularios.formularioEdicionPlatos import FormularioEdicionPlatos

from web.models import Platos,Empleados

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')

def MenuPlatos(request):

    PlatosConsultados=Platos.objects.all()

    formulario=FormularioEdicionPlatos()

    diccionarioEnvio={
        'platos':PlatosConsultados,
        'formulario':formulario
    }

    return render(request, 'menuPlatos.html',diccionarioEnvio)


def MostrarEmpleados(request):

    EmpleadosConsultados=Empleados.objects.all()
    
    for empleado in EmpleadosConsultados:
         print(empleado.foto)

    diccionarioEnvioEmpleados={
        'empleados':EmpleadosConsultados
    }

    return render(request, 'mostrarEmpleados.html',diccionarioEnvioEmpleados)


def VistaPlatos(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioPlato':formulario,
        'bandera':False
    }


    #preguntamos si existe alguna peticion de tipo POST,asociada a la vista 

    if request.method=='POST':
        #deveriamos capturar los datos del fomrulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente (VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturar data
            datosPlato=datosDelFormulario.cleaned_data
            #Creamos un objeto del tipo MODELO PLATO
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )

            #Intentamos llevar el objeto plato nuevo a La BD
            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print(error,error)

    return render(request,'platos.html',datosParaTemplate)
#---------------------------------------------------------------------------------------------------------------------------

def VistaEmpleados(request):

    formulario=FormularioEmpleados()
    datosParaTemplate={
        'formularioEmpleados':formulario,
        'bandera':False
    }


    #preguntamos si existe alguna peticion de tipo POST,asociada a la vista 

    if request.method=='POST':
        #deveriamos capturar los datos del fomrulario
        datosDelFormulario=FormularioEmpleados(request.POST)
        #verificar si los datos llegaron correctamente (VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturar data
            datosEmpleado=datosDelFormulario.cleaned_data
            #Creamos un objeto del tipo MODELO PLATO
            empleadoNuevo=Empleados(
                nombre=datosEmpleado["nombreEmpelado"],
                apellido=datosEmpleado["apellidoEmpelado"],
                foto=datosEmpleado["fotoEmpelado"],
                cargo=datosEmpleado["cargoEmpleado"],
                salario=datosEmpleado["salarioEmpelado"],
                contacto=datosEmpleado["contactoEmpleado"],

            )

            #Intentamos llevar el objeto plato nuevo a La BD
            try:
                empleadoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("EXITO GUARDANDO LOS DATOS")

            except Exception as error:
                datosParaTemplate["bandera"]=False
                print(error,error)

    return render(request,'empleados.html',datosParaTemplate)

#---------------------------------------------------------------------------------------------------------------------------


