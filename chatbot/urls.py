from django.urls import path
import views

urlpatterns = [
    path('', views.chatbot, name='chatbot')
]