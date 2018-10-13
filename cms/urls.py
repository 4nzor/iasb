from django.urls import path
from . import views
urlpatterns = [
    path('', views.redir),
    path('index/<slug:slug>/' ,views.index )


]