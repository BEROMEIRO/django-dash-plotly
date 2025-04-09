from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')), 
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
