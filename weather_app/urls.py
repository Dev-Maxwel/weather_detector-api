from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    
    
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), 
         name="reset_password"),
    
    path('reset_password_done', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_done.html"),
         name="password_reset_done"),
    
    path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
         name="password_reset_confirm"),
    
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), 
         name="password_reset_complete"),
    
]
