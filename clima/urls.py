from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('history/add', views.HistorialCreateView.as_view()),
    path('history/all', views.HistorialViewList.as_view()),
]