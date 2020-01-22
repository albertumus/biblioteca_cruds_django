from django.shortcuts import render
from django.db.models import Q

from django.http import FileResponse, Http404

from catalogo.models import Autor, Libro

def home(request):

    query = request.GET.get("q")


    if query:
        autores_libros_filtrados = Libro.objects.filter( Q(titulo__icontains=query) | Q(autor_libro=query) )  
        print(autores_libros_filtrados)
        return render(request, 'core/home.html', {"autores_libros_filtrados": autores_libros_filtrados})
    else:
        return render(request, 'core/home.html', {})

    return render(request, 'core/home.html')


