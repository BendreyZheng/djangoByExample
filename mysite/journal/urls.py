from django.urls import path
from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.journal_list, name='journal_list'),
    path('<int:id>/', views.profile_detail, name='profile_detail'),
]
