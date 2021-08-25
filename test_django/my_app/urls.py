from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.sayhello, name='Home'),
    path('explain/', views.explain, name="explain"),
    path('result/', views.sayhello, name='result'),
    path('explain/detail/<explainid>', views.detail, name="detail"),
    path('Multiplication/', views.Multiplication),
    path('division/', views.division),

]
