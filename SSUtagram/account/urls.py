from django.urls import path
from . import views


urlpatterns=[
    path('account/signup',views.signup,name="signup"),
    path('account/login',views.login,name="login"),
    path('account/logout',views.logout,name="logout"),
]