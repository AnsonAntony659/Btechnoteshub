from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:scheme_id>/',views.year_list,name='year_list'
    ),
     path(
        'detail/<int:year_id>/',
        views.year_detail,
        name='year_detail'
    ),
]