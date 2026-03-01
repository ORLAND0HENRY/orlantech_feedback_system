
from django.urls import path
from . import views

app_name = 'orlantech_feedback'

urlpatterns = [
    path('submit/', views.submit_feedback, name='submit'),
]