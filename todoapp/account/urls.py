from django.urls import path
from.views import *


urlpatterns=[
    path('reg',RegView.as_view(),name='reg'),
    path('lgout',LogoutView.as_view(),name='lgout')

]