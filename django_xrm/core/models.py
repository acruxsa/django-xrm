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

    created_at = models.DateTimeField(verbose_name=u"Fecha de creación",
                                      auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name=u"Fecha de modificación",
                                       auto_now=True)


class IdentificationType(BaseModel):
    """

    """
    name = models.CharField(u'Nombre', max_length=127)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name = u"Tipo de identifcación"
        verbose_name_plural = u"Tipos de Identificación"


class Person(BaseModel):
    """

    """

    firstname = models.CharField(u'Nombre', max_length=255)
    lastname = models.CharField(u'Apellido', max_length=255, blank=True)
    identification_type = models.ForeignKey(IdentificationType, verbose_name=u'Tipo de Identificación')
    identification = models.CharField(u'Identificación', max_length=255)
    imagen_perfil = models.ImageField(upload_to=partial(uploadFilename, 'profiles_images'),
                                      blank=True, null=True)
    comments = models.TextField(u'Observaciones', blank=True)

    def __unicode__(self):
        if self.lastname:
            return u"{}, {}".format(self.lastname, self.firstname)
        else:
            return u"{}".format(self.firstname)

    class Meta:
        verbose_name = u"Persona"
        verbose_name_plural = u"Personas"


class Contact(BaseModel):
    """

    """
    name = models.CharField(u'Nombre', max_length=255)
    is_email = models.BooleanField(u'¿Es E-mail?')
    is_phone = models.BooleanField(u'¿Es Teléfono?')
    is_sms = models.BooleanField(u'¿Es SMS?')
    is_geo = models.BooleanField(u'¿Es Geolocalización?')
    is_skype = models.BooleanField(u'¿Es skype?')

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name = u"Contacto"
        verbose_name_plural = u"Contactos"


class PersonContact(BaseModel):
    """

    """
    value = models.CharField(u'Valor', max_length=255)
    contact = models.ForeignKey(Contact, verbose_name=u'Tipo de contacto', null=False, related_name='contacts')
    person = models.ForeignKey(Person, verbose_name=u'Persona', null=False)

    def __unicode__(self):
        return u"{} {} {}".format(self.person, self.contact, self.value)

    class Meta:
        verbose_name = u"Dato de Persona"
        verbose_name_plural = u"Datos de Personas"
