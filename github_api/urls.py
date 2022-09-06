from django.urls import path
from .views import github_Profile_view


urlpatterns = [
        path('github_profile/', github_Profile_view,name='github_Profile_view'),
        

    ]