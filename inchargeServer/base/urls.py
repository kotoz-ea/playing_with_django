from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('telemetry/', views.telemetry, name='telemetry')

]
