from django.urls import path
from . import views
urlpatterns = [
    path('', views.Get_Post_Test, name='get'),
    path('login/', views.login, name='login'),
    path('post/<int:pk>', views.Put, name='put'),
    path('cookies/', views.Cookies, name='cookies'),
    path('cookies/', views.Cookies, name='cookies'),
    path('transfer-money', views.TransferMoney, name='cookies'),
]
