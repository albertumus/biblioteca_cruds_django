from django.conf.urls import url, include
from cruds_adminlte.urls import crud_for_app, crud_for_model

from administracion.views import RegistroCRUD

registrocrud = RegistroCRUD()


urlpatterns = [
    url(r'', include(registrocrud.get_urls())),
]
