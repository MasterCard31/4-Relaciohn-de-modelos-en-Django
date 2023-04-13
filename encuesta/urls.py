from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    # ex: /encuesta/2/
    path('<int:pregunta_id>/', views.detalle, name='detalle'),
    # ex: /encuesta/2/resultados/
    path('<int:pregunta_id>/voto/', views.resultados, name='resultados'),
    # ex: /encuesta/2/voto/
    path('<int:pregunta_id>/resultados/', views.votar, name='votar'),

]