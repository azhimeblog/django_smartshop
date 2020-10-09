from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    #path('<partnumber:partnumber>/', views.ProductDetail.as_view(), name='product_detail'),
]