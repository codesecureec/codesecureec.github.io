from django.shortcuts import render
from .templates.form import ContactForm

def contactar(request):
    data = {
        'form': ContactForm()
    }
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Pronto nos pondremos en contacto contigo."
        else:
            data['form'] = formulario

    return render(request, 'contact.html', data)

