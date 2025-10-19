from django.urls import path
from reminders import views

urlpatterns = [
    path('reminders/', views.ReminderList.as_view()),
    path('reminders/<int:pk>/', views.ReminderDetail.as_view()),
]
