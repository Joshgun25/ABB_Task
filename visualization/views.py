from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import *

# Frequently Asked Questions View
class FrequentlyAskedQuestionsChartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'charts_page.html'

    def get(self, request):
        chart_json = generate_frequently_asked_questions()
        return Response({'chart_json': chart_json})

# QA Length Chart View
class QADataChartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'charts_page.html'

    def get(self, request):
        chart_json = generate_length_of_questions_answers()
        return Response({'chart_json': chart_json})

# Time Series Chart View 
class TimeSeriesChartView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'charts_page.html'

    def get(self, request):
        chart_json = generate_time_series()
        return Response({'chart_json': chart_json})

# Questions Word Cloud View
class WordCloudView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'charts_page.html'

    def get(self, request):
        chart_json = generate_word_cloud()
        return Response({'chart_json': chart_json})