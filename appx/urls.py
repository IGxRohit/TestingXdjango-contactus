
from django.urls import path
from appx import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('savedata',views.savedata,name="savedata"),
    path('services/',views.services,name="services"),
    path('delete/<int:id>',views.delete),
    path('upd/<int:id>',views.updateform),
    path('updating/<int:id>',views.update)

]