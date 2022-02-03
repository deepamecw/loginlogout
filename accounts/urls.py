from django.urls import path
from .import views

urlpatterns = [
   path('',views.home,name ='home'),
   path('register/',views.registerPage,name ='register'),
   path('login/',views.loginPage,name ='login'),
   path('logout/',views.logoutpage,name = 'logout'),
   path('python/',views.python,name = 'python'),
]