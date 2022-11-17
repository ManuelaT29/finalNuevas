#LOS FORMULARIOS DE DJANGO SON CLASES

from django import forms


class FormularioEmpleados(forms.Form):

    #CREANDO ATRIBUTO PARA ACRGAR EL SELECTOR
    OPCIONES=(
        (1,'Cocinero'),
        (2,'Ayudante'),
        (3,'Mesero'),
        (4,'Admin')
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    nombreEmpelado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=5,
        label="Nombre Empleado"
    )

    apellidoEmpelado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        max_length=20,
        label="Apellido Empleado"
    )

    fotoEmpelado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Foto Empleado"
    )

    cargoEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES,
        label="Cargo Empleado"
    )
    
    salarioEmpelado=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Salario Empleado"
    )
    contactoEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        label="Numero Contacto"
    )