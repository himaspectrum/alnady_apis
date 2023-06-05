from django.urls import path
from . import views

urlpatterns = [
    path('account_items_list/', views.AccountItemsList.as_view(), name='account_items_list'),
    path('account_items/', views.AccountItems.as_view(), name='account_items'),
    path('analytic_item/', views.AnalyticitemList.as_view(), name='analytic_items'),
]
