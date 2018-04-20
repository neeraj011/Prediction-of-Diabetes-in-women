from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserHome
from . import views

app_name='gui'
urlpatterns =[
	
	
	url(r'^input/$',UserHome.as_view(), name='input'),
	url(r'^train/$', views.model_form_train ,name='train'),
	url(r'^$', auth_views.login, {'template_name': 'admin-home.html'}, name='admin_home'),
	url(r'^graph/$', views.get_image ,name='graph'),
	url(r'^gra/$', auth_views.login, {'template_name': 'graph.html'}, name='gra'),
	
		
]