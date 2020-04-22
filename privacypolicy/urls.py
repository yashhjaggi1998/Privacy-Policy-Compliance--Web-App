from . import views
from django.conf.urls import url


urlpatterns = [
	url(r'^$' , views.HomeView.as_view() , name = 'home'),
	url(r'^aboutus$' , views.AboutUsView.as_view() , name = 'aboutus'),
	url(r'^input/$' , views.InputView.as_view() , name = 'input'),
	url(r'^input/v1/$' , views.v1View.as_view() , name = 'v1'),
	url(r'^input/v2/$' , views.v2View.as_view() , name = 'v2'),
	url(r'^input/output/$' , views.call_model.as_view(), name = 'output'),
	#url(r'^(?P<question_id>[0-9]+)/vote/$' , views.vote , name = 'vote'),
]
