from django.urls import path
from .views import home, results_view, radio

urlpatterns = [  
    path('', home, name='home'),
    path('try/', radio, name='radio'),
    path('result/', results_view, name='results-view'),
]
