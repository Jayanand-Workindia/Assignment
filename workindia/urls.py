from . import views
from django.urls import path

urlpatterns = [
    path('jobs/<candidate_id>', views.get_jobs, name='get_jobs'),
    path('action/<candidate_id>', views.store_action, name='store_action')
]