from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/<int:feed_id>',views.detail,name='detail'),
    path('feed/new',views.new, name='new'),
    path('feed/create',views.create,name='create'),
]