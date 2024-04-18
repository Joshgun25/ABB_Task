from django.shortcuts import redirect
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .forms import UploadFileForm, URLForm
from .utils import openai_integration
from .models import Answer, Question
from .scraping import scrape_website

# Scrape Data View
class ScrapeDataView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'scrape_data.html'

    def get(self, request):
        form = URLForm()
        return Response({'form': form})

    def post(self, request):
        form = URLForm(request.data)
        if form.is_valid():
            # Retrieve URL
            url = form.cleaned_data['url']
            try:
                scrape_website(url)
                return redirect('data_upload')  # Redirect to data upload page after successful scrape
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        return Response({'form': form}, status=400)

# Scraped Data Upload View
class DataUploadView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'data_upload.html'

    def get(self, request):
        form = UploadFileForm()
        return Response({'form': form})
    
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve file
            uploaded_file = form.cleaned_data['file']

            # Assign file name and content to django session
            request.session['uploaded_file_name'] = uploaded_file.name
            request.session['uploaded_file_contents'] = uploaded_file.read().decode('utf-8')
            return redirect('chat_bot')  # Redirect to chat page after successful upload
        else:
            return Response({'form': form})

# Chat Bot View
class ChatView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_page.html'

    def get(self, request):
        return Response()
    
    def post(self, request):
        # Retrieve question text and file name
        question_text = request.data.get('question')
        uploaded_file_name = request.session.get('uploaded_file_name')

        # Generate answer by openAI
        answer_text = openai_integration(question_text, uploaded_file_name)

        # Save question and answer to database
        question = Question.objects.create(text=question_text)
        Answer.objects.create(question=question, text=answer_text)

        return JsonResponse({'answer': answer_text})

# Menu Page View
class MenuPageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'menu_page.html'

    def get(self, request):
        return Response()