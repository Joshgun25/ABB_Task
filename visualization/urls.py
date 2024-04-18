from django.urls import path
from .views import *
urlpatterns = [
    path('frequently_asked/', FrequentlyAskedQuestionsChartView.as_view(), name='frequently_asked'),
    path('length/', QADataChartView.as_view(), name='length'),
    path('time_series/', TimeSeriesChartView.as_view(), name='time_series'),
    path('word_cloud/', WordCloudView.as_view(), name='word_cloud'),
]
