from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TYPE_EXTENSION_FILE, File
from .serializers import FileSerializer
from .controller import ControllerData


class FileUploadView(APIView):
    """
    Upload file to server and save it to DB.
    """

    parser_class = (FileUploadParser, JSONParser)

    def get(self, request, format=None):
        snippets = File.objects.all()
        serializer = FileSerializer(snippets, many=True)
        return Response(serializer.data)


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


class TableChangeFieldNameView(APIView):
    """
    Coloumn names change in table.
    """

    parser_class = (JSONParser,)


    def put(self, request, *args, **kwargs):
        try:
            print(f'tableName - {request.data["tableName"]}')
            print(f'fieldsName - {request.data["fieldsName"]}')
            data = request.data["fieldsName"]
            controller = ControllerData(table_name=request.data["tableName"])
            # print(len(data))
            if controller.check_table_is_exist():
                if controller.check_table_columns_for_changes(data):
                    controller.change_column_name(data)
                else:
                    return Response(f'Wrong data')
            else:
                return Response('Table does not exist')

        except Exception as err:
            print(str(err))
        return Response('OK')


class TableChangeFieldPositionView(APIView):
    """
    Coloumn names change in table.
    """

    parser_class = (JSONParser,)


    def put(self, request, *args, **kwargs):
        try:
            print(f'tableName - {request.data["tableName"]}')
            print(f'fieldsName - {request.data["fieldsName"]}')
            data = request.data["fieldsName"]
            controller = ControllerData(table_name=request.data["tableName"])
            # print(len(data))
            if controller.check_table_is_exist():
                if controller.check_table_columns_for_changes(data):
                    controller.change_column_name(data)
                else:
                    return Response(f'Wrong data')
            else:
                return Response('Table does not exist')

        except Exception as err:
            print(str(err))
        return Response('OK')
