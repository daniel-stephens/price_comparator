from django.urls import path
from .views import home, results_view

urlpatterns = [  
    path('', home, name='home'),
    #path('results/', results_view, name='Results'),
    path('result/', results_view, name='results-view'),
]
