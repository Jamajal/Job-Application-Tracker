from django.urls import path
from .views import read_insert_job_application, read_update_delete_job_application

urlpatterns = [
    path('api/v1/job_application', read_insert_job_application),
    path('api/v1/job_application/<int:pk>', read_update_delete_job_application)
]

