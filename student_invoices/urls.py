from django.urls import path
from . import views

urlpatterns = [
    path('create_student_invoice/', views.CreateStudentInvoice.as_view(), name='create_student_invoice'),
    # path('cancel_student_invoice/', views.CancelStudentInvoice.as_view(), name='cancel_student_invoice'),
]
