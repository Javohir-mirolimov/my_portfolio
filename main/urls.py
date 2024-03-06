from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index_url'),
    path('create_contact_us/', create_contact_us, name='create_contact_us_url')
]