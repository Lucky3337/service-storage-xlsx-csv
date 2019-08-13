from .database import Table


class ControllerDB:

    def __init__(self, table_name, file_path='', field_name_list=list, type_fields_dict=dict, rows_list=list, *args, **kwargs):
        self.table_name = table_name
        self.file_path = file_path
        self.field_name_list = field_name_list
        self.type_fields_dict = type_fields_dict
        self.rows_list = rows_list
        self.table = Table(
            table_name=self.table_name,
            file_path=self.file_path,
            field_name_list=self.field_name_list,
            type_fields_dict=self.type_fields_dict,
        )

    def run_xlsx(self):
        result, response = self.table.create()
        if result:
            self.table.insert_data_from_xlsx_file(data=self.rows_list)

    def run_csv(self):
        result, response = self.table.create()
        if result:
            self.table.insert_data_from_csv_file(data=self.rows_list)

