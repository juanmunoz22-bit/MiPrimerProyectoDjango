from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    # Creamos el formulario de contacto llamado formulario_contacto
    formulario_contacto = FormularioContacto()

    # Si el método es POST, es decir, si el usuario envia el formulario
    if request.method == 'POST':
        # Creamos una instancia de formulario_contacto con los datos del formulario recibido
        formulario_contacto = FormularioContacto(request.POST)
        # Comprobamos si el formulario es valido
        if formulario_contacto.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario forms.py
            nombre =request.POST.get('nombre','')
            email = request.POST.get('email','')
            contenido = request.POST.get('contenido','')

            #creamos el email
            email = EmailMessage('Mensaje desde App Django',
            'El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}'.format(nombre,email,contenido),
            '', ['juan.pablo982206@gmail.com'],reply_to=[email])

            try:
                # Enviamos el email
                email.send()
                # Si se envía correctamente, redireccionamos a la página principal
                return redirect('/contacto/?valido')
            except:
                # Si no se envía correctamente, redireccionamos a la página principal
                return redirect('/contacto/?error')

            
            
    return render(request, 'contacto/contacto.html', {'formulario_contacto': formulario_contacto})


