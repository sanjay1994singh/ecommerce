from django.urls import path
from . import views
urlpatterns = [
    path('user_signup/',views.user_signup,name='user_signup')
]