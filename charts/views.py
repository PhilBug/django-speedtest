from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import JsonResponse, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from speedtest import Speedtest
from logging import getLogger
from .models import TestResult

logger = getLogger(__name__)


def index(request):
    return render(request, 'charts/index.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        id_list, result_list, label_list = [], [], []

        test_result = TestResult.objects.all().values(
            'result', 'id', 'date', 'username')
        for test in test_result:
            logger.info(
                f"{test['username']} - {test['id']}, {test['result']}, {test['date'].strftime('%H:%M:%S %b %d %Y')}"
            )

            id_list.append(test['id'])
            result_list.append(test['result'])

            label_list.append(test['date'].strftime(
                '%H:%M:%S %b %d %Y') + ' user: ' + test['username'])

        data = {
            'labels': label_list,
            'default': result_list,
        }
        return Response(data)


class RunSpeedTest(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        st = Speedtest()
        test_result = '{:.2f}'.format(st.download() / 1024 / 1024)
        username = request.POST['username']

        test_instance = TestResult.objects.create(
            result=test_result, username=username)
        logger.info(f'{test_result} mb/s')
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
