import os
from django.db import models

# Create your models here.

class PMGBPModel(models.Model):
    model = models.FileField(upload_to='compiled_models/')
    parameters = models.FileField(upload_to='model_parameters/')

    def __str__(self):
        return self.name()

    def name(self):
        return os.path.basename(self.model.path)

class SBMLfile(models.Model):
    file = models.FileField(upload_to='sbml_files/')
    model = models.ForeignKey(PMGBPModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.filename().replace('.xml', '')

    def filename(self):
        return os.path.basename(self.file.name)

    def model_ready(self):
        return not self.model is None