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
        # For *.xlsx pattern files. Crete table if it is not exist and write dato in the table DB
        result, response = self.table.create()
        if result:
            self.table.insert_data_from_xlsx_file(data=self.rows_list)

    def run_csv(self):
        # For *.csv pattern files. Crete table if it is not exist and write dato in the table DB
        result, response = self.table.create()
        if result:
            self.table.insert_data_from_csv_file(data=self.rows_list)

    def change_column_name(self, column_name_list):
        table_columns = self.table.get_columns_informations()
        print(table_columns)
        print(table_columns[1][0])
        for key, value in column_name_list.items():
            int(key, int(table_columns[int(key)][2]))
            if int(key)+1 == int(table_columns[int(key)][2]):
                try:
                    self.table.change_column_name(table_columns[int(key)][0], value)
                except Exception as ex:
                    print(str(ex))
                print('pizdata')





class ControllerData(ControllerDB):

    def check_table_is_exist(self):
        return self.table.check_table_is_exist()

    def check_table_columns_for_changes(self, field_name_list):
        table_columns = self.table.get_columns_informations()
        print(f'field_name_list - {field_name_list}')
        print(f'table_columns - {table_columns}')
        if len(field_name_list) <= len(table_columns) - 1:
            first_key = ''

            # check that field_name_list is sequences of numbers between 1 to len(table_columns) - 1
            for key, value in field_name_list.items():
                if int(key) <= len(table_columns) - 1:
                    if first_key == '':
                        first_key = int(key)
                    elif (first_key + 1) == int(key):
                        first_key = int(key)
                    else:
                        return False
                else:
                    return False

            # compare columns between yourself. It will be different value
            for index in range(1,len(field_name_list)+1):
                for ind in range(index+1, len(field_name_list)+1):
                    if field_name_list[str(index)] == field_name_list[str(ind)]:
                        return False

            # compare columns between database and new. It will not be equals each other
            for index in range(1,len(table_columns)):
                for ind in range(index, len(field_name_list)):
                    print(ind, table_columns[index][0], field_name_list[str(ind)])
                    if table_columns[index][0] == field_name_list[str(ind)]:
                        return False

            return True
        else:
            return False





