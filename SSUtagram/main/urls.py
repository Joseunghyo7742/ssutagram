from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('feed/<int:feed_id>',views.detail,name='detail'),
    path('feed/new',views.new, name='new'),
    path('feed/create',views.create,name='create'),
    path('feed/delete/<int:feed_id>',views.delete,name='delete'),
    path('feed/edit/<int:feed_id>',views.edit,name='edit'),
    path('feed/update/<int:feed_id>',views.update,name='update'),
    path('profile/<int:author_id>',views.profile,name='profile'),
    path('myprofile/',views.myProfile,name='myprofile'),
    
]