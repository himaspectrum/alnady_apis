from django.urls import path
from . import views

urlpatterns = [
    path('staff_payments_list/<slug:identification_id>/', views.StaffPaymentsList.as_view(), name='staff_payments_list'),
    path('show_staff_payment_details/<slug:payment_id>/', views.ShowStaffPaymentDetails.as_view(), name='show_staff_payment_details'),
    path('edit_staff_member/', views.EditStaffMember.as_view(), name='edit_staff_member'),
]
