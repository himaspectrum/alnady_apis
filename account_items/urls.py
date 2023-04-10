from django.urls import path
from . import views

urlpatterns = [
    path('account_items_list/', views.AccountItemsList.as_view(), name='account_items_list'),
    path('account_items_edit/<slug:name>/<slug:account_code>/', views.AccountItemsEdit.as_view(), name='account_items_edit'),
]
