from django.urls import path
from attachments import views

urlpatterns = [
    path('attachments/', views.AttachmentList.as_view()),
    path('attachments/<int:pk>/', views.AttachmentDetail.as_view()),
]