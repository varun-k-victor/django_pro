from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home),
    path('form/',views.form),
    path('message/',views.message)
]