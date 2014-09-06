# -*- coding: utf-8 -*-
from functools import partial

from django.db import models

from .utils import uploadFilename


class BaseModel(models.Model):
    """
    Todos los modelos deben heredar de esta clase.

    """
    class Meta:
        abstract = True

    creado_el = models.DateTimeField(verbose_name=u"Fecha de creación",
            auto_now_add=True)
    modificado_el = models.DateTimeField(verbose_name=u"Fecha de modificación",
            auto_now=True)


class IdenticationType(BaseModel):
    """

    """
    name = models.CharField(u'Nombre', max_length=127)


class Person(BaseModel):
    """

    """

    firstname = models.CharField(u'Nombre', max_length=255)
    lastname = models.CharField(u'Apellido', max_length=255)
    identification_type = models.ForeignKey(IdenticationType, verbose_name=u'Tipo de Identificación', null=False)
    identification = models.CharField(u'Identificación', max_length=255)
    imagen_perfil = models.ImageField(upload_to=partial(uploadFilename, 'profiles_images'),
                                      blank=True, null=True)


class ContactType(BaseModel):
    """

    """
    name = models.CharField(u'Nombre', max_length=255)
    email = models.EmailField(u'E-mail')
    phone = models.CharField(u'Teléfono' )
