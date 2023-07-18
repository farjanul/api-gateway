from django.urls import path, re_path as url

from apps.apigateway.views import ApiGatewayView

app_name = 'api_gateway'

urlpatterns = [
    url(r'(?P<path>.*)', ApiGatewayView.as_view(), name='api_gateway_view'),
]
