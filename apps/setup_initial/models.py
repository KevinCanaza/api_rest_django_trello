from django.db import models

# Create your models here.

class SetupInitialModel(models.Model):
    id = models.AutoField(primary_key =	True)
    state = models.BooleanField('Estado', default= True)
    create_at = models.DateField('Fecha de Creación', auto_now=False, auto_now_add= True)
    update_at = models.DateField('Fecha de Modificacion', auto_now= True, auto_now_add= False)
    deleted_at = models.DateField('Fecha de Eliminarcion', auto_now= True, auto_now_add= False)

    class Meta:

        abstract = True
        verbose_name = 'SetupInitialModel'
        verbose_name_plural = 'SetupInitialModels'


