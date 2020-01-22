from django.shortcuts import render
from cruds_adminlte.crud import CRUDView

from catalogo.models import Tematica, Autor, Editorial, Libro 
from catalogo.forms import LibroAddForm, LibroUpdateForm, LibroViewForm ,AutorCRUDForm

class LibroCRUD(CRUDView):

    model = Libro
    check_login = True
    check_perms = True

    add_form = LibroAddForm
    update_form = LibroUpdateForm
    detail_form = LibroViewForm

    views_available=['create','list', 'detail', 'update']

    search_fields = ['titulo__icontains']
    list_filter = ['autor_libro', 'editorial_libro']

    list_fields = ['titulo', 'autor_libro', 'editorial_libro']
    display_fields = ['titulo', 'autor_libro', 'editorial_libro', 'documento']

    related_fields = ['editorial_libro']
    

class AutorCRUD(CRUDView):

    model = Autor
    check_login = True
    check_perms = True

    add_form = AutorCRUDForm
    update_form = AutorCRUDForm
    
    views_available=['create','list', 'detail', 'update']

    search_fields = ['nombre__icontains']
    list_filter = ['temas']

    list_fields = ['nombre', 'nacimiento', 'ciudad']
    display_fields = ['nombre', 'nacimiento', 'ciudad']
    

class EditorialCRUD(CRUDView):

    model = Editorial
    check_login = False
    check_perms = False

    views_available=['create','list', 'detail', 'update']

    list_fields = ['nombre', 'fecha_creacion', 'ciudad']
    display_fields = ['nombre', 'fecha_creacion', 'ciudad']

class TematicaCRUD(CRUDView):

    model = Tematica
    check_login = True
    check_perms = True

    views_available=['create','list', 'detail', 'update']


