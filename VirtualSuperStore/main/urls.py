from .views import ProductDetailView, CategoryDetailView,BaseView
from django.urls import path

urlpatterns = [
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('', BaseView.as_view() ,name='base'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail' )

]
