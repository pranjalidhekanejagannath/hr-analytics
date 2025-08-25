from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_employee, name='add_employee'),
    # path('all/', views.all_employees, name='all_employees'),
    # path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    # path('promote/<int:emp_id>/', views.promote_employee, name='promote_employee'),
]