from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views import View
from django.conf.urls import include,url

from privacypolicy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adding a new URL
    #path('model/', views.call_model.as_view())
    path('privacypolicy/', include('privacypolicy.urls')),
]