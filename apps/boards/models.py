from django.db import models
from simple_history.models import HistoricalRecords

from apps.setup_initial.models import SetupInitialModel

# Create your models here.

class Board(SetupInitialModel):

    name = models.CharField('Nombre',max_length=50, blank= False, null = False, unique= True)
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'

    def __str__(self):
        return self.name


class TaskList(SetupInitialModel):

 
    title = models.CharField('Titulo', max_length=50, unique = True, null= False, blank = False)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, verbose_name= 'Tablero')
    
    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Lista de Tarea'
        verbose_name_plural = 'Listas de Tareas'

    def __str__(self):
        return self.title

class Task(SetupInitialModel):

    title = models.CharField('Titulo', max_length=109, unique = True, null= False, blank = False)
    description = models.CharField('Descripcion', max_length=100, unique = True, null= True, blank = True)
    assigne = models.CharField('Asignado', max_length=100, unique = False, null= True, blank = True)
    task_list_id = models.ForeignKey(TaskList, on_delete=models.CASCADE, verbose_name= 'Lista de Tarea')

    historical = HistoricalRecords()


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value    

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.title
