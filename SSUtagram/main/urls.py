from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/<int:feed_id>',views.detail,name='detail'),
]