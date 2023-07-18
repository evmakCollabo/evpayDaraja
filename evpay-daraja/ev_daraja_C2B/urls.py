from django.urls import path
from . import views
from .views import confirmationURL,validationURL,register_url,C2B_API

urlpatterns = [
    path('',C2B_API.as_view()),
    # path('api/v1/.as_view()',),
    path('confirmation/',views.confirmationURL,name="confirmation"),
    path('validationURL/',views.validationURL,name="validationURL"),
    path('register_url/',views.register_url,name="register_url"),
    path('simulate_C2B_API/',views.simulate_C2B_API,name="simulate_C2B_API"),
]