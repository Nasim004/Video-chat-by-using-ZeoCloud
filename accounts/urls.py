from django.urls import path
from accounts import views


urlpatterns = [
    path('',views.Home,name='homepage'),
    path('meeting',views.meetings,name='meeting'),

]
