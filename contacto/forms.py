#Crea un formulario en django con campos requeridos nombre y email pero el campo contenido no es requerido para la página de contacto
#Labels para los campos del formulario nombre y email

from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    contenido = forms.CharField(label="Contenido", required=False, widget=forms.Textarea)

