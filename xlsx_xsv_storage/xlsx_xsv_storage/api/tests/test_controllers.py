from django.test import TestCase
from xlsx_xsv_storage.api.controller import ControllerDB, ControllerData
from xlsx_xsv_storage.api.models import File


class TestController(TestCase):

    def setUp(self):
        self.field_name_list_xlsx, self.type_fields_dict_xlsx, self.rows_list_xlsx = File.read_xlsx_file(
            'xlsx_xsv_storage/static/tests/fruits2.xlsx')
        self.table_name_csv = 'fruits2'
        self.controller_xlsx = ControllerDB(
            table_name=self.table_name_csv,
            field_name_list=self.field_name_list_xlsx,
            type_fields_dict=self.type_fields_dict_xlsx,
            rows_list=self.rows_list_xlsx,
        )
        self.field_name_list, self.type_fields_dict, self.rows_list = File.read_csv_file(
            'xlsx_xsv_storage/static/tests/test1.csv')
        self.table_name_xlxs = 'test1'
        self.controller_xlsx = ControllerDB(
            table_name=self.table_name_xlxs,
            field_name_list=self.field_name_list,
            type_fields_dict=self.type_fields_dict,
            rows_list=self.rows_list,
        )

    def test_change_column_name_xlxs(self):
        pass

    def test_check_table_is_exist_xlxs(self):
        controller_data = ControllerData(table_name=self.table_name_xlxs)
        self.assertEqual(type(controller_data.check_table_is_exist()), bool)

    def test_check_table_is_exist_csv(self):
        controller_data = ControllerData(table_name=self.table_name_csv)
        self.assertEqual(type(controller_data.check_table_is_exist()), bool)

    def test_check_table_columns_for_changes_xlxs(self):
        data1 = {
            "tableName": self.table_name_xlxs,
            "fieldsName": {
                "1": "dddaadta",
                "2": "asdzxc",
                "3": "asdd"

            }
        }

        controller_data = ControllerData(table_name=self.table_name_xlxs)
        self.assertEqual(type(controller_data.check_table_columns_for_changes(data1)), bool)

    def test_check_table_columns_for_changes_csv(self):
        data1 = {
            "tableName": self.table_name_csv,
            "fieldsName": {
                "1": "dddaadta",
                "2": "asdzxc",
                "3": "asdd"

            }
        }

        controller_data = ControllerData(table_name=self.table_name_csv)
        self.assertEqual(type(controller_data.check_table_columns_for_changes(data1)), bool)


