from django.test import TestCase
from xlsx_xsv_storage.api.models import File
from datetime import datetime


class TestFile(TestCase):

    def setUp(self):
        pass
        # File.objects.create(name="cat", sound="meow")

    def test_str_get_type_value(self):
        self.assertEqual(File.str_get_type_value('222'), 'int')
        self.assertEqual(File.str_get_type_value('11.23'), 'float')
        self.assertEqual(File.str_get_type_value('Hello work213'), 'varchar')
        self.assertEqual(File.str_get_type_value('Hello work213' * 30), 'text')
        self.assertEqual(File.str_get_type_value('23.07.1995 13:33:00'), 'datetime')
        self.assertEqual(File.str_get_type_value('23.07.1995'), 'datetime')
        self.assertEqual(File.str_get_type_value('1995.07.21'), 'datetime')
        self.assertEqual(File.str_get_type_value('13:33:00'), 'time')
        self.assertEqual(File.str_get_type_value(''), '')

    def test_read_xlsx_file(self):
        field_name_list, type_fields_dict, rows_list = File.read_xlsx_file('xlsx_xsv_storage/static/tests/fruits2.xlsx')
        test_field_name_list = ['apple', 'pear', 'cherry', 'tomato']
        test_type_fields_dict = {
            1: 'varchar',
            2: 'text',
            3: 'int',
            4: 'text'
        }
        self.assertListEqual(field_name_list,test_field_name_list)
        self.assertDictEqual(type_fields_dict, test_type_fields_dict)
        self.assertTrue(field_name_list)
        self.assertTrue(type_fields_dict)
        self.assertTrue(rows_list)

    def test_read_csv_file(self):
        field_name_list, type_fields_dict, rows_list = File.read_csv_file('xlsx_xsv_storage/static/tests/test1.csv')
        test_field_name_list = [' field1' ,' field2' ,' field3' ,' field4' ,' field5' ,' field6' ]
        test_type_fields_dict = {
            1: 'int',
            2: 'int',
            3: 'time',
            4: 'datetime',
            5: 'float',
            6: 'text'
        }
        self.assertTrue(field_name_list)
        self.assertTrue(type_fields_dict)
        self.assertTrue(rows_list)
