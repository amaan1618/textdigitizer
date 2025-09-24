from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('upload/', views.upload_note, name='upload_note'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='notes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
