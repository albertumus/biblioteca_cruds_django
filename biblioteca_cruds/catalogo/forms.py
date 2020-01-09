from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from crispy_forms.bootstrap import TabHolder, Tab, FormActions

from django.utils.translation import ugettext_lazy as _

from cruds_adminlte import DatePickerWidget

from catalogo.models import Libro, Autor

class LibroCRUDForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'autor_libro', 'editorial_libro']

    def __init__(self, *args, **kwargs):
        super(LibroCRUDForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Basic information'),
                    Field('titulo', wrapper_class="col-md-6"),
                    Field('autor_libro', wrapper_class="col-md-6"),
                    Field('editorial_libro', wrapper_class="col-md-12"),
                ),
                Tab(
                    _('Other information'),
                    
                )
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )

class AutorCRUDForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = ['nombre', 'nacimiento', 'ciudad', 'temas']
        widgets = {
                'nacimiento': DatePickerWidget(attrs={'format': 'mm/dd/yyyy',
                                            'icon': 'fa-calendar'}),
        }