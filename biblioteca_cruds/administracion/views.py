from django.shortcuts import render

from cruds_adminlte.crud import CRUDView

from catalogo.models import Registro

class RegistroCRUD(CRUDView):

    model = Registro
    check_login = False
    check_perms = False

    views_available=['list', 'detail']

    paginate_by = 10
    paginate_template = 'cruds/pagination/prev_next.html'
    paginate_position = 'Bottom'

    list_filter = ['content_type', 'tipo_acceso']