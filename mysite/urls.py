from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import re_path
from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    re_path(r'^slide4/$', core_views.slide4, name='slide4'),
    re_path(r'^slide5/$', core_views.slide5, name='slide5'),
    re_path(r'^slide7/$', core_views.slide7, name='slide7'),
    re_path(r'^slide8/$', core_views.slide8, name='slide8'),
    re_path(r'^slide9/$', core_views.slide9, name='slide9'),
    re_path(r'^slide10/$', core_views.slide10, name='slide10'),
    re_path(r'^slide11/$', core_views.slide11, name='slide11'),

]
