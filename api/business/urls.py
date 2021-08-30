from django.urls import path
from .views import BusinessRegisterView, ListBusinessView, RateBusinessView
urlpatterns = [
    path('businesses/register', BusinessRegisterView.as_view()),
    path('businesses', ListBusinessView.as_view()),
    path('businesses/<str:pk>', ListBusinessView.as_view()),
    path('rate', RateBusinessView.as_view())
]
