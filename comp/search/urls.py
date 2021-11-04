from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    #path('results/', SearchView.as_view(), name='results')   
]
