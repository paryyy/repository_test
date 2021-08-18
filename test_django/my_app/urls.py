from django.urls import path
from . import views

urlpatterns = [
    path('', views.sayhello),
    path('explain/', views.explain)
]
