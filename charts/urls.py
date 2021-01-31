from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='charts'),
    path('api/chart/data/', views.ChartData.as_view(), name='chart_data'),
    path('api/test/run/', views.RunSpeedTest.as_view(), name='test_run'),
]
