from django.urls import path
from .views import LoggedInUser, RegisterUserView, LoginView
urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('login', LoginView.as_view()),
    path('user', LoggedInUser.as_view())
]
