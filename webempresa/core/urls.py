#creamos nuestras urls solo para core importando solo las urls de esta app

# importamos django urls y importamos path
from django.urls import path
# tamabien hacemos referencia al archivo views del mismo directorio
from . import views


# Colocamos las URLS
urlpatterns = [
  path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('services/', views.services, name = "services"),
    path('store/', views.store, name = "store"),
    path('contact/', views.contact, name = "contact"),
    path('blog/', views.blog, name = "blog"),
    path('sample/', views.sample, name = "sample"),
    
]