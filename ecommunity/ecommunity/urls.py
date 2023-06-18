"""
URL configuration for ecommunity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ecommunity_app.views import APILogin, APISertificateForCovid_19, APINarkUchet, APIZapisKVrachu
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'uchet', APINarkUchet)

router_for_sertificate = routers.SimpleRouter()
router_for_sertificate.register(r'sertificate', APISertificateForCovid_19)

router_for_Login = routers.SimpleRouter()
router_for_Login.register(r'login', APILogin)

router_zapis_k_vrachu = routers.SimpleRouter()
router_zapis_k_vrachu.register(r'zapis-k-vrachu', APIZapisKVrachu)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_for_Login.urls)), # Login
    path('api/', include(router_for_sertificate.urls)), # Sertificate
    path('api/', include(router.urls)) # Uchet
    # path('api/Uchet/', APINarkUchet.as_view({'get': 'list'})), #post
    # path('api/Uchet/<int:pk>/', APINarkUchet.as_view({'put': 'update'}))
    
]
