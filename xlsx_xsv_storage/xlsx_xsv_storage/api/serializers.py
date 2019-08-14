from rest_framework import serializers
from .models import File
from django.utils.timezone import now, pytz
from django.conf import settings


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ["file", ]

    def create(self, validated_data):
        user_timezone = pytz.timezone(settings.TIME_ZONE)
        file = str(validated_data["file"]).split('.')
        print(f'validated_data - {validated_data}')
        print(f'validated_data - {validated_data["file"]}')

        obj, created = File.objects.update_or_create(
            table_name=file[0],
            type_file=file[1],
            defaults={
                'file': validated_data['file'],
                'date_updated': now().astimezone(user_timezone)
            },
        )
        print(obj)

        return obj
