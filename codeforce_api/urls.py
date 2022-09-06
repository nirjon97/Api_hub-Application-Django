from .views import codeforce_user_view
from django.urls import path

urlpatterns = [
        path('user_details/',codeforce_user_view,name='codeforce_user_view'),

    ]