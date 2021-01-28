from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='charts'),
    path('api/data/', views.get_data, name='get_data'),
    path('api/chart/data/', views.ChartData.as_view(), name='chart_data'),
]
