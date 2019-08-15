from django.test import TestCase
from xlsx_xsv_storage.api.database import Table


class TestTable(TestCase):

    def test_type_fields(self):
        table = Table()
        TYPE_FIELDS = {
            'text': 'text',
            'varchar': 'varchar(128)',
            'int': 'integer',
            'float': 'float',
            'datetime': 'timestamptz',
            'time': 'time',
        }
        self.assertDictEqual(table.TYPE_FIELDS, TYPE_FIELDS)

    def test_postgresql_type_fields_tp_python(self):
        table = Table()
        POSTGRESQL_TYPE_FIELDS_TO_PYTHON = {
            'text': 'text',
            'varchar': 'varchar',
            'int4': 'int',
            'float8': 'float',
            'timestamptz': 'datetime',
            'time': 'time',
        }
        self.assertDictEqual(table.POSTGRESQL_TYPE_FIELDS_TO_PYTHON, POSTGRESQL_TYPE_FIELDS_TO_PYTHON)
