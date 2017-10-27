from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.login_page),                               # RENDERS LOGIN PAGE
    url(r'^register_account$', views.register_account),         # VALIDATES POST DATA, CREATES USER, RETURN REDIRECT TO LOGIN PAGE
    url(r'^login$', views.login),                               # VALIDATES POST DATA, ALLOWS OR DENIES LOGIN, REDIRECTS TO APP PAGE  
]