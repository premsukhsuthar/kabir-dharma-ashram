from django.urls import path
from .views import home
from . import views
urlpatterns = [
    path('', home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kabir/', views.kabir, name='kabir'),
    path('ashram/', views.ashram_page, name='ashram'),
    path('trust/', views.trust, name='trust'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('donate/', views.donate, name='donate'),


]

