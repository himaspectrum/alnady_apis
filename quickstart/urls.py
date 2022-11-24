from django.urls import path
from . import views

app_name='Cosmeticsshortname'

urlpatterns = [
    path('Cosmeticsshortname', views.CosmeticsshortnameCreate.as_view()),
    path('Cosmeticsshortnames/', views.ListCosmeticsshortnameView.as_view(), name="Cosmeticsshortnames"),
    path("Cosmeticsshortname/<slug:pk>/", views.DetailCosmeticsshortnameView.as_view(), name="Cosmeticsshortname"),
    path("Cosmeticsshortname/delete/<slug:pk>/", views.DestoryCosmeticsshortnameView.as_view(), name="delete_Cosmeticsshortname"),
]