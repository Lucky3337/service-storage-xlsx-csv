from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('file/upload', views.FileUploadView.as_view()),
    path('table/change_field_name', views.TableChangeFieldNameView.as_view()),
    path('', TemplateView.as_view(template_name="snippets/index.html"))
    # path('', views.SwaggerSchemaView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)
