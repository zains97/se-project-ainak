from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index, name='Home'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('search/', views.search, name='search'),
    path('wishlist/<int:id>', views.wishlist, name="wishlist"),
    path('viewglasses/<int:id>', views.viewglasses, name="viewglasses"),
    path('account/<int:id>', views.account, name="account"),
    path('sell/', views.sell, name="sell"),
    path('buy/<int:id>', views.buy, name="buy"),
    path('vission-test/', views.vissiontest, name="vission-test"),
    path('glassesdetail/<int:myid>', views.glassesdetail, name='glassesdetail'),
    path('sunglasses/', views.sunglasses, name='sunglasses'),
    path('eyeglasses/', views.eyeglasses, name='eyeglasses'),
    path('contact/', views.contact, name='ContactUs'),
    path('about/', views.about, name='about'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('delivery/', views.delivery, name='delivery'),
    path('allusers/', views.allusers, name='allusers'),

]

