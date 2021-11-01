from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('telemetry/<str:pk>/', views.telemetry, name='telemetry')

]
