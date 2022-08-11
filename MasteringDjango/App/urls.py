


from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index,name="index"),
    path('', views.Index.as_view(),name="index"),
    # path('contactUs/', views.contactUs,name="contactUs"),
    path('contactUs/', views.ContactUs.as_view(),name="contactUs"),

    # Authentication Endpoints
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginViewUser.as_view(), name="login"),
    path('signupseller/', views.RegisterViewSeller.as_view(), name="signupseller"),

    
   
]
