from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return render(request, 'charts/index.html', {'customers': 10})

def get_data(reqest):
    data = {
        'sales': 100,
        'customers': 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            'sales': 100,
            'customers': 10,
        }

        return Response(data)
