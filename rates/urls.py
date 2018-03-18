from django.urls import path

from . import views

app_name = 'rates'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:currency_id>/', views.detail, name='detail'),
]