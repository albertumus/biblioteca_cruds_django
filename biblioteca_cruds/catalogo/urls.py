from django.conf.urls import url, include
from catalogo.views import LibroCRUD, AutorCRUD, TematicaCRUD, EditorialCRUD

librocrud = LibroCRUD()
autorcrud = AutorCRUD()
tematicacrud = TematicaCRUD()
editorialcrud = EditorialCRUD()

urlpatterns = [
    url(r'', include(librocrud.get_urls())),
    url(r'', include(autorcrud.get_urls())),
    url(r'', include(tematicacrud.get_urls())),
    url(r'', include(editorialcrud.get_urls()))
]
