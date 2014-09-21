from django.shortcuts import render
from django.views.generic import ListView

from core.models import Person


class PersonListView(ListView):
    template_name = "frontend/person_list.html"
    queryset = Person.objects.all()


person_list = PersonListView.as_view()