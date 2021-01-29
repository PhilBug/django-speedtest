from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from speedtest import Speedtest

from .models import TestResult


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
        id_list, result_list, dates_list = [], [], []

        test_result = TestResult.objects.all().values('test_result', 'id', 'test_date')
        for test in test_result:
            # for debugging
            print(f"{test['id']}, {test['test_result']}, {test['test_date'].strftime('%H:%M:%S %b %d %Y')}")

            id_list.append(test['id'])
            result_list.append(test['test_result'])
            dates_list.append(test['test_date'].strftime('%H:%M:%S %b %d %Y'))

        labels = dates_list
        default_items = result_list

        data = {
            'labels': labels,
            'default': default_items,
        }
        return Response(data)


class RunSpeedTest(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        st = Speedtest()
        test_result = '{:.2f}'.format(st.download() / 1024 / 1024)
        print(test_result)  # in megabytes

        test_instance = TestResult.objects.create(test_result=test_result)
        test_instance.save()
        content = {
            'message': 'successful test run',
            'value': test_result,
        }
        return Response(content, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        content = {
            'message': 'nothing to see here',
            'value': None,
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)
