from django.urls import path
from . import views

urlpatterns = [
    path('account_items', views.AccountItemsView.as_view(), name='test'),
]
