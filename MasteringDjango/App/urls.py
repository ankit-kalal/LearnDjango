


from django.urls import path
from . import views



app_name = 'App'

urlpatterns = [
    # path('', views.index,name="index"),
    path('', views.Index.as_view(),name="index"),
    path('contackus/', views.contackus,name="contackus"),
    
   
]
