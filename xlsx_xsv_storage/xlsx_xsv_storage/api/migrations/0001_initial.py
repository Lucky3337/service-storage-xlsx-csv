# Generated by Django 2.2.4 on 2019-08-14 17:57

from django.db import migrations, models
import django.utils.timezone
import xlsx_xsv_storage.api.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=xlsx_xsv_storage.api.storage.OverwriteStorage(), upload_to='')),
                ('type_file', models.CharField(choices=[('csv', 'csv'), ('xlsx', 'xlsx')], max_length=4)),
                ('table_name', models.CharField(max_length=120, verbose_name='Название файла')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки')),
                ('date_updated', models.DateTimeField(default=None, null=True, verbose_name='Дата обновления')),
            ],
        ),
    ]
