from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('file/upload', views.FileUploadView.as_view()),
    path('', views.SwaggerSchemaView.as_view())
    # path('video/<int:pk>/', views.VideoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
