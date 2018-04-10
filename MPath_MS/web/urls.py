from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_sbml', views.upload_sbml_form, name='upload_sbml_form'),
    path('sbml_files', views.sbml_files, name='sbml_files'),
    path('remove_sbml_file', views.remove_sbml_file, name='remove_sbml_file'),
]