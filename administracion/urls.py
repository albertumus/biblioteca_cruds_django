from django.conf.urls import url, include
from cruds_adminlte.urls import crud_for_app, crud_for_model
from django.contrib.auth import views as auth_views

from django.contrib.auth.models import User

from administracion.views import RegistroCRUD, UsuarioCRUD , logout


registrocrud = RegistroCRUD()
usuariocrud = UsuarioCRUD()


urlpatterns = [
    url(r'accounts/login/', auth_views.LoginView.as_view(), name='login_custom'),
    url(r'logout/', logout, name='logout'),
    url(r'', include(registrocrud.get_urls())),
    url(r'', include(usuariocrud.get_urls())),
]



