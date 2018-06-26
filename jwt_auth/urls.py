from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.contrib.auth.views import logout

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('logout/', logout),
    path('refresh/', refresh_jwt_token),
    path('verify/', verify_jwt_token),
]