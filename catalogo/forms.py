from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from crispy_forms.bootstrap import TabHolder, Tab, FormActions

from django.utils.translation import ugettext_lazy as _

from cruds_adminlte import DatePickerWidget

from catalogo.models import Libro, Autor

class LibroViewForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = ['titulo', 'autor_libro']

    def __init__(self, *args, **kwargs):
        super(LibroViewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Información Básica'),
                    Field('titulo', wrapper_class="col-md-6"),
                    Field('autor_libro', wrapper_class="col-md-6"),
                    Field('creado_por', wrapper_class="col-md-6"),
                    Field('editorial_libro', wrapper_class="col-md-12"),
                    Field('documento', wrapper_class="col-md-12"),
                    HTML("""<iframe src="http://127.0.0.1:8000/media/documents/ase.pdf" 
                    style="width:100%; 
                    height:150%;" 
                    frameborder="0"></iframe>
                    """)
                ),
                Tab(
                    _('Otra Información'),
                    
                )
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
            )
        )

class LibroAddForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LibroAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Información Básica'),
                    Field('titulo', wrapper_class="col-md-6"),
                    Field('autor_libro', wrapper_class="col-md-6"),
                    Field('creado_por', wrapper_class="col-md-6"),
                    Field('editorial_libro', wrapper_class="col-md-12"),
                    Field('documento', wrapper_class="col-md-12"),
                ),
                Tab(
                    _('Otra Información'),
                    
                )
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
            )
        )

class LibroUpdateForm(forms.ModelForm):

    class Meta:
        model = Libro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LibroUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['creado_por'].disabled = True
        disabled_widget = forms.Select(attrs={'disabled': True})

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Información Básica'),
                    Field('titulo', wrapper_class="col-md-6" ),
                    Field('autor_libro', wrapper_class="col-md-6"),
                    Field('creado_por', wrapper_class="col-md-8"),
                    Field('editorial_libro', wrapper_class="col-md-12"),
                    Field('documento', wrapper_class="col-md-12")
                ),
                Tab(
                    _('Otra Información'),
                    
                )
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
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