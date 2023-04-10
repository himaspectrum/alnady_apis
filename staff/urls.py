from django.urls import path
from . import views

urlpatterns = [
    path('all_staff_payments', views.HrPayslipView.as_view(), name='hr_payslip_list'),
    path('staff_payments_list/<slug:identification_id>/', views.StaffPaymentsList.as_view(), name='hr_payslip_detail'),
]
