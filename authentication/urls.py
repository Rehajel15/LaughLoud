from django.urls import path
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path("", views.choose, name='choose'),
    path("signin/", views.SignIn, name='signin'),
    path("signup/", views.SignUp, name='signup'),
    path("signout/", views.SignOut, name='signout'),
    path("deleteacc/", views.DeleteAccount, name='deleteacc')
]
