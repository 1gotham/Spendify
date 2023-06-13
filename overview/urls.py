from django.urls import path
from . import views

urlpatterns = [
    path('overview/<int:year>/<str:month>/', views.overview, name='index')
]