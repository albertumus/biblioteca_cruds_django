from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from cruds_adminlte.crud import CRUDView

from administracion.models import Registro, Usuario

class RegistroCRUD(CRUDView):

    model = Registro
    check_login = True
    check_perms = True

    views_available=['list', 'detail']

    paginate_by = 10
    paginate_template = 'cruds/pagination/prev_next.html'
    paginate_position = 'Bottom'

    list_filter = ['content_type', 'tipo_acceso']

class UsuarioCRUD(CRUDView):

    model = Usuario
    check_login = True
    check_perms = True

    views_available=['create', 'update' , 'list', 'detail']

    list_fields = ['id', 'last_login', 'username', 'biografia', 'localizacion', 'edad', 'date_joined', 'first_name']
    #display_fields = ['id', 'last_login', 'username', 'biografia', 'localizacion', 'edad', 'date_joined', 'first_name', , 'staff_status']


@login_required
def logout(request):
    
    if ( request.user.is_authenticated ) :
        django_logout(request)
        return HttpResponseRedirect('/')

    else:
        return None