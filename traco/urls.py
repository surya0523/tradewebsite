from django.urls import path
from . import views
from .views import partner_view 
 
urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.home, name="home"),
    path('partner/', partner_view, name='partner'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path("verify-otp/", views.verify_otp_view, name="verify_otp"),
    path("send-otp/", views.send_otp_view, name="send_otp"), 
    path("about/", views.about_view, name="about"),
]
 