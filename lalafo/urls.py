from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello),
    path('kyrgyzstan/transport/', views.my_transport, name='transport'),
    path('kyrgyzstan/nedvijimost/', views.nedvijimost, name='nedvijimost'),
    # path('kyrgyzstan/uslugi/', views.uslugi),
    # path('kyrgyzstan/remonty/', views.remonty),
    # path('kyrgyzstan/domisad/', views.domisad),
    # path('kyrgyzstan/electronika/', views.electronika),
    # path('kyrgyzstan/work/', views.work),
    # path('kyrgyzstan/equipmentforbusiness/' , views.equipmentforbusiness),
    # path('kyrgyzstan/sportandhobbies/', views.sportandhobbies),
    # path('kyrgyzstan/animals/', views.animals),
    # path('kyrgyzstan/denskiymir/', views.detskiymir),
]