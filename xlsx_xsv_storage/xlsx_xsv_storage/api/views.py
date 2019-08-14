from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TYPE_EXTENSION_FILE

from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers



from .serializers import FileSerializer


class FileUploadView(APIView):
    """
    Upload file to server and write it to DB.
    """

    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        print(f"request.data['file'] - {request.data['file']}")
        file = str(request.data['file']).split('.')
        for item in TYPE_EXTENSION_FILE:
            # compare input file type with allowable types | csv and xlsx
            if file[1] in item[0]:
                file_serializer = FileSerializer(data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return Response(file_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("file type error", status=status.HTTP_400_BAD_REQUEST)






class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)
