from django.urls import path
from . import views
urlpattern =[
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
   # path('login/',),
    path('register/', views.registerView,name="register_url"),
   # path('logout/',),
    ]