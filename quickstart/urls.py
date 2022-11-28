from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('product', views.ListProductSerializer.as_view()),
    path("Cosmeticsshortname/<slug:pk>/", views.DetailCosmeticsshortnameView.as_view(), name="Cosmeticsshortname"),
]