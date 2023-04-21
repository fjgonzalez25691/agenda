from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView
)
#
from rest_framework.generics import(
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
#
from .models import (
    Person,
    Reunion
)

from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonSerializer2,
    ReunionSerializer,
    PersonSerializer3,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer
)

class PersonListApiView(ListAPIView):
    # serializar en un Json.
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        return Person.objects.all()

class ListaPersonas(ListView):
    
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    
    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = "persona/lista.html"



class PersonSearchApiView(ListAPIView):
    # serializar en un Json.
    template_name = "persona/buscar_persona.html"
    serializer_class = PersonSerializer
    
    def get_queryset(self):
        #filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )
        

class PersonCreateAPIView(CreateAPIView):
    serializer_class = PersonSerializer
    
class PersonDetailAPIView(RetrieveAPIView):
        
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonDeleteAPIView(DestroyAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonUpdateAPIView(UpdateAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    
class PersonApilista(ListAPIView):
    """ 
        Vista para interactuar con serializadores
    """
    serializer_class = PersonaSerializer
    def get_queryset(self):
        return Person.objects.all()
    
class PersonApilista2(ListAPIView):
    """ 
        Vista para interactuar con serializadores
    """
    serializer_class = PersonSerializer2
    
    def get_queryset(self):
        return Person.objects.all()
    
class ReunionApilista(ListAPIView):
  
    serializer_class = ReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.all()

class PersonApilista3(ListAPIView):
    
    serializer_class = PersonSerializer3
    def get_queryset(self):
        return Person.objects.all().order_by('id')

class ReunionApilista2(ListAPIView):
  
    serializer_class = ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()
    
class ReunionApiListaLink(ListAPIView):
    
    serializer_class = ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()
    
class PersonPaginationList(ListAPIView):
    """
    Vista personas con paginación
    """
    
    serializer_class = PersonSerializer3
    pagination_class = PersonPagination 
    
    def get_queryset(self):
        return Person.objects.all().order_by('id')
    
class ReunionByPersonJob(ListAPIView):
    
    serializer_class = CountReunionSerializer
    
    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()