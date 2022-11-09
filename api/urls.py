from django.urls import path
from django.views.generic import TemplateView

from api.infrastructure.views import *

app_name = 'api'

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('coin/names/', ApiClientNames.as_view(), name="get_names"),
    path('coin/<str:symbol>/<str:date>', ApiClientClose.as_view(), name="get_close"),
    path('mxprofit/<str:symbol>/<str:start>/<str:end>', ApiClientMaxProfit.as_view(), name="get_max_profit")
]
