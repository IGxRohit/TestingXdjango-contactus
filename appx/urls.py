
from django.urls import path
from appx import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('savedata',views.savedata,name="savedata"),
<<<<<<< HEAD
    path('services/',views.services,name="services"),
    path('delete/<int:id>',views.delete,)
=======
    path('services/',views.services,name="services")
>>>>>>> 15e090cdaf9aac0b34ba82e0366fa3ab391b7393

]