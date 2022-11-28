from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('product', views.ListProduct.as_view()),
    path('product_batches', views.ProductBatches.as_view()),
    path("Cosmeticsshortname/<slug:pk>/", views.DetailCosmeticsshortnameView.as_view(), name="Cosmeticsshortname"),
]