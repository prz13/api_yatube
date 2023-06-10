from rest_framework.views import APIView
from rest_framework.response import Response


class MyAPIView(APIView):
    def get(self, request):
        
        data = {'message': 'Привет, мир!'}
        return Response(data)

    def post(self, request):
        
        data = request.data
        return Response(data, status=201)