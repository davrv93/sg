from uuid import uuid4
from django.db import models


class ActoAcademico(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, editable=False)
    nombre = models.CharField(
        unique=True, max_length=150,
        blank=False, null=False)
   
    class Meta:
        verbose_name = 'Acto académico'
        verbose_name_plural =  'Acto académico'
        default_permissions = ()
        permissions = (
            ('add_actoacademico',
             'Puede agregar ActoAcademico'),
            ('change_actoacademico',
             'Puede actualizar ActoAcademico'),
            ('delete_actoacademico',
             'Puede eliminar ActoAcademico'),
            ('list_actoacademico',
             'Puede listar ActoAcademico'),
            ('get_actoacademico',
             'Puede obtener ActoAcademico'),
        )
        db_table = 'sg_acto_academico'

