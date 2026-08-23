from django.urls import path
from . import views 

urlpatterns = [
    path("<int:course_id>/",views.department_list,name="department_list")
]