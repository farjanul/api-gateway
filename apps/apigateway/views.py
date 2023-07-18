from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.apigateway.api_gateway import APIGateway


class ApiGatewayView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = APIGateway(request).forward_request()
        return Response(response.json(), status=response.status_code)

    def post(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        response = APIGateway(request).forward_request(data)
        return Response(response.json(), status=response.status_code)

    def patch(self, request, *args, **kwargs):
        data = request.body.decode('utf-8')
        response = APIGateway(request).forward_request(data)
        return Response(response.json(), status=response.status_code)

    def delete(self, request, *args, **kwargs):
        response = APIGateway(request).forward_request()
        if response.status_code == 204:
            return Response({'message': 'DELETE request processed successfully.'}, status=response.status_code)
        return Response(response.json(), status=response.status_code)
