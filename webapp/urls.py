from django.urls import path
from .views import DataUploadView, ChatView, ScrapeDataView, MenuPageView

urlpatterns = [
    path('scrape/', ScrapeDataView.as_view(), name='scrape_data'),
    path('data_upload/', DataUploadView.as_view(), name='data_upload'),
    path('chat_bot/', ChatView.as_view(), name='chat_bot'),
    path('', MenuPageView.as_view(), name='menu'),
]
