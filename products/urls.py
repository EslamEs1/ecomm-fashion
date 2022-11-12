from django.urls import path
from .views import ShopListView, ShopDetailView


app_name = 'products'


urlpatterns = [
    path('', ShopListView.as_view(), name='shop-list'),
    path('<slug:slug>/', ShopListView.as_view(), name='filter-list'),
    path('details/<slug:slug>/', ShopDetailView.as_view(), name='shop-detail'),
]
