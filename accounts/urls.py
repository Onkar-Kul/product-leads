from django.urls import path

from accounts.views import UserRegistrations, UserLoginView, LogoutView

urlpatterns = [
    path('registration/', UserRegistrations.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),

]
