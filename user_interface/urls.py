from django.urls import path
from .views import registration_page, home_page, login_page, dashboard

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', registration_page, name='registration_page'),
    path('login/', login_page, name='login_page'),
    path('dashboard/', dashboard, name='dashboard'),

]
