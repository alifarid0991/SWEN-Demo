from django.urls import path

from . import views

urlpatterns = [
    path('upload'    , views.upload_video  , name='upload_video'),
    path('info'      , views.get_video_info      , name='get_video_info'),
    path('search'    , views.seach_video   , name='search_in_video_info'),
]