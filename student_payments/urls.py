from django.urls import path
from . import views

urlpatterns = [
    path('bank_list/', views.BankList.as_view(), name='bank_list'),
    path('invoice_transaction/', views.StudentInvoiceTransaction.as_view(), name='bank_list'),

]
