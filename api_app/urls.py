from .views import all_api_list
from django.urls import path,include


urlpatterns = [
        path('',all_api_list,name='all_api_list'),
        path('weather/',include('weather_api.urls')),
        path('codeforce/',include('codeforce_api.urls')),
        path('github/', include('github_api.urls')),

    ]