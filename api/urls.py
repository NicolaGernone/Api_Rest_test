from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken import views

from api.infrastructure.views import ApiClient

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('coin/<str:name>', ApiClient.as_view(), name="get_names"),
    path('coin/<str:symbol>/<str:date>', ApiClient.as_view(), name="get_close"),
    path('data/<str:start>/<str:end>', ApiClient.as_view(), name="get_max_profit")
]
