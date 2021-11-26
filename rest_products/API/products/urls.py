from django.urls import path

from .views import CategoryListCreate, CategoryDeleteUpdate, ProductDeleteUpdate, ProductListCreate, ProviderDeleteUpdate, ProviderListCreate

urlpatterns = [
    path('category/', CategoryListCreate.as_view()),
    path('category/<int:pk>/', CategoryDeleteUpdate.as_view()),
    path('provider/', ProviderListCreate.as_view()),
    path('provider/<int:id>/', ProviderDeleteUpdate.as_view()),
    path('product/', ProductListCreate.as_view()),
    path('product/<int:id>/', ProductDeleteUpdate.as_view()),
]
