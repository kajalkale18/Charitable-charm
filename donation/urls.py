from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.index, name= 'index'),
    path("donateNow/",views.pay_now, name= 'paynow'),
    path("success/",views.success, name= 'success'),
    path("about/",views.about, name= 'about'),

]
