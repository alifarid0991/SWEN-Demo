from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

import json

from .models import *
from .validators import *

from django.urls import reverse

# build_task_url = lambda x,y : ("http://localhost:8000%s?task_id=%s" % (reverse(x) , y))

from .utils.VideoIndexer import VideoIndexer

CONFIG = {
    'SUBSCRIPTION_KEY': '42a4abcbdb144820b3650f58d95828b1',
    'LOCATION': 'trial',
    'ACCOUNT_ID': '8046da76-6527-4646-bc4b-38de633bec1a'
}

vi = VideoIndexer(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)

@require_http_methods(["GET"])
@csrf_exempt
def upload_video(request):
    form = UploadForm(request.GET)
    if form.is_valid() :
        video_url  = request.GET.get('video_url', None)
        video_name = request.GET.get('video_name', None)
        language   = request.GET.get('language', None)
        # https://topcs.blob.core.windows.net/public/Machine-Learning-in-IoT-solutions_high.mp4
        data = vi.upload_to_video_indexer_by_url(video_url,video_name,language)
        return JsonResponse({'status' : 'success' , 'message' : data })
    else :
        return JsonResponse({'status' : 'error' , 'message' : 'try again !' })

@require_http_methods(["GET"])
@csrf_exempt
def get_video_info(request):
    form = InfoForm(request.GET)
    if form.is_valid() :
        video_id  = request.GET.get('video_id', None)
        data = vi.get_video_info(video_id)
        return JsonResponse(data)
    else :
        return JsonResponse({'status' : 'error' , 'message' : 'try again !' })



@require_http_methods(["GET"])
@csrf_exempt
def seach_video(request):
    form = SearchForm(request.GET)
    if form.is_valid() :
        query      = request.GET.get('query', None)
        language   = request.GET.get('language', None)
        data = vi.search_in_video(query,language)
        return JsonResponse(data)
    else :
        return JsonResponse({'status' : 'error' , 'message' : 'try again !' })
