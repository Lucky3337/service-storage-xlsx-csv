from django.db import connection
import psycopg2


class Table:

    def __init__(self, table_name='', file_path='', field_name_list=list, type_fields_dict=dict, *args, **kwargs):
        self.table_name = table_name
        self.file_path = file_path,
        self.field_name_list = field_name_list
        self.type_fields_dict = type_fields_dict
        self.TYPE_FIELDS = {
            'text': 'text',
            'varchar': 'varchar(128)',
            'int': 'integer',
            'float': 'float',
            'datetime': 'timestamptz',
            'time': 'time',
        }
        self.POSTGRESQL_TYPE_FIELDS_TO_PYTHON = {
            'text': 'text',
            'varchar': 'varchar',
            'int4': 'int',
            'float8': 'float',
            'timestamptz': 'datetime',
            'time': 'time',
        }

    def _make_sql_create_table(self):
        query = f"CREATE TABLE {str(self.table_name)} (pk serial PRIMARY KEY, "
        for index in range(len(self.field_name_list)):
            query += f"{self.field_name_list[index]} {self.TYPE_FIELDS[str(self.type_fields_dict[index+1])]} NULL"

            # adding comma at the and row before last field
            if index != len(self.field_name_list)-1:
                query += ", "
        query += ");"
        return query

    def _make_sql_insert_data_into_table(self, data):
        query = f"INSERT INTO {self.table_name} ("

        for index in range(len(self.field_name_list)):
            query += f"{self.field_name_list[index]}"

            if index != len(self.field_name_list)-1:
                query += ", "
            else:
                query += ") values"

        for i, dictionary in enumerate(data):
            row_to_insert = ' ('
            for index in range(len(self.field_name_list)):
                if dictionary[self.field_name_list[index]] == 'NULL':
                    row_to_insert += f"{dictionary[self.field_name_list[index]]}"
                else:
                    row_to_insert += f"'{dictionary[self.field_name_list[index]]}'"

                if index != len(self.field_name_list) - 1:
                    row_to_insert += ", "
                else:
                    row_to_insert += ")"

            query += row_to_insert
            if i != len(data) - 1:
                query += ', '
            else:
                query += ";"
        print(query)
        return query


    def _make_sql_columns_informations(self):
        query = f"SELECT column_name, udt_name, ordinal_position \
                                  FROM information_schema.columns \
                                    WHERE table_schema = 'public' \
                                   AND table_name   = '{self.table_name}';"

        return query

    def change_column_name(self,column_name, new_column_name):
        query = f"ALTER TABLE {self.table_name} \
                                RENAME COLUMN {column_name} TO {new_column_name};"
        with connection.cursor() as cursor:
            cursor.execute(query)


    def get_columns_informations(self):
        query = self._make_sql_columns_informations()

        with connection.cursor() as cursor:
            cursor.execute(query)
            table_coloumns = cursor.fetchall()
        return table_coloumns

    def check_table_is_exist(self):
        query = f"SELECT EXISTS ( \
           SELECT 1 \
           FROM pg_tables \
           WHERE schemaname = 'public' \
           AND tablename = '{self.table_name}' \
           );"


        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                return cursor.fetchone()[0]
            except Exception:
                return False

    def _compare_columns_beetwin_file_and_table(self):
        query = self._make_sql_columns_informations()

        table_coloumns = self.get_columns_informations()
        print(f'field_name_list - {self.field_name_list}')
        print(f'type_fields_dict - {self.type_fields_dict}')
        print(table_coloumns)

        list_matching = []
        for index, coloumn in enumerate(table_coloumns):
            midl_result = {}
            dict_field = {}

            if index == 0:
                continue
            # compare coloumn names
            if self.field_name_list[index-1] == coloumn[0]:

                # compare coloumn types
                if self.type_fields_dict[index] == self.POSTGRESQL_TYPE_FIELDS_TO_PYTHON[coloumn[1]]:
                    midl_result['matching'] = 'true'
                else:
                    dict_field['type'] = [self.type_fields_dict[index], coloumn[1]]
                    midl_result['matching'] = dict_field
                    # compare coloumn types
            elif self.type_fields_dict[index] == self.POSTGRESQL_TYPE_FIELDS_TO_PYTHON[coloumn[1]]:
                dict_field['name'] = [self.field_name_list[index-1], coloumn[0]]
                midl_result['matching'] = dict_field
            else:
                dict_field['name'] = [self.field_name_list[index-1], coloumn[0]]
                dict_field['type'] = [self.type_fields_dict[index], coloumn[1]]
                midl_result['matching'] = dict_field

            list_matching.append(midl_result)
        print(list_matching)
        return list_matching

    def create(self):
        table_exist = self.check_table_is_exist()
        coloumn_name = self._compare_columns_beetwin_file_and_table()
        print(f'table_exist - {table_exist}')
        if table_exist is False:
            sql_create_table = self._make_sql_create_table()
            print(sql_create_table)
            with connection.cursor() as cursor:
                cursor.execute(sql_create_table)
            return True, f'Table {self.table_name} is created'
        else:
            mismatch_list = []
            for coloumn in coloumn_name:
                if coloumn['matching'] == 'true':
                    continue
                else:
                    mismatch_list.append(coloumn)
            if len(mismatch_list) > 0:
                return True, f'Table {self.table_name} already have created'
            else:
                return False, mismatch_list

    def insert_data_from_xlsx_file(self, data):
        query = self._make_sql_insert_data_into_table(data)
        with connection.cursor() as cursor:
            cursor.execute(query)

    def insert_data_from_csv_file(self, data):
        query = self._make_sql_insert_data_into_table(data)
        with connection.cursor() as cursor:
            cursor.execute(query)

