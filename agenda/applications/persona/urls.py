from django.urls import path, re_path
#
from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersonas.as_view(),
        name='personas'
    ),
    path(
        'api/persona/lista/',
        views.PersonListApiView.as_view(),
       
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista'
    ),
    path(
        'api/persona/search/<kword>',
        views.PersonSearchApiView.as_view(),
       
    ),
    path(
        'api/persona/create/',
        views.PersonCreateAPIView.as_view(),
       
    ),
    path(
        'api/persona/detail/<pk>/',
        views.PersonDetailAPIView.as_view(),
        name='detalle'
       
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonDeleteAPIView.as_view(),
       
    ),
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateAPIView.as_view(),
       
    ),
    path(
        'api/persona/modificar/<pk>/',
        views.PersonRetrieveUpdateAPIView.as_view(),
       
    ),
    path(
        'api/personas/',
        views.PersonApilista.as_view(),
       
    ),
    path(
        'api/personas2/',
        views.PersonApilista2.as_view(),
       
    ),
    path(
        'api/reuniones/',
        views.ReunionApilista.as_view(),
       
    ),
    path(
        'api/personas3/',
        views.PersonApilista3.as_view(),
       
    ),
    path(
        'api/reuniones2/',
        views.ReunionApilista2.as_view(),
       
    ),
    path(
        'api/reuniones-link/',
        views.ReunionApiListaLink.as_view(),
       
    ),
    path(
        'api/personas/pagination',
        views.PersonPaginationList.as_view(),
       
    ),
    path(
        'api/reunion/por-job',
        views.ReunionByPersonJob.as_view(),
       
    ),
] 