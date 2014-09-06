from django.contrib import admin

from .models import Contact, Person, IdentificationType, PersonContact

admin.site.register(Contact)
admin.site.register(Person)
admin.site.register(IdentificationType)
admin.site.register(PersonContact)
