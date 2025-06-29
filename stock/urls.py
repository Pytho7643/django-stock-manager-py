from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.detail, name='detail'),
]
