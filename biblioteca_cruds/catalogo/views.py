from django.shortcuts import render
from cruds_adminlte.crud import CRUDView

from catalogo.models import Tematica, Autor, Editorial, Libro 
from catalogo.forms import LibroCRUDForm, AutorCRUDForm

class LibroCRUD(CRUDView):

    model = Libro
    check_login = False
    check_perms = False

    add_form = LibroCRUDForm

    search_fields = ['titulo__icontains']
    list_filter = ['autor_libro', 'editorial_libro']

class AutorCRUD(CRUDView):

    model = Autor
    check_login = False
    check_perms = False

    add_form = AutorCRUDForm
    update_form = AutorCRUDForm

    search_fields = ['nombre__icontains']
    list_filter = ['temas']

class EditorialCRUD(CRUDView):

    model = Editorial
    check_login = False
    check_perms = False

class TematicaCRUD(CRUDView):

    model = Tematica
    check_login = False
    check_perms = False

