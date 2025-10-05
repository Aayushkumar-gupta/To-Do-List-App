from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from main.views import home, create, index

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),  
    path('home/', home, name='home'),
    path('create/', create, name='create'),
    path('list/<int:id>/', index, name='index'),
]
