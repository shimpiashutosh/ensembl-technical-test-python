from uk.ac.ebi.ensembl.search.gene.tests.util.sql_commands_test import insert_into_gene_autocomplete_table, \
    select_all_from_gene_autocomplete_table


class PrepareTestData:
    def __init__(self, db_connection_test_obj):
        self.db_connection = db_connection_test_obj

    def prepare_test_data_success_case(self):
        sample_data = [
            ('homo_sapiens', 'BRCA1'),
            ('homo_sapiens', 'BRCA2'),
        ]
        cursor = self.db_connection.conn.cursor()
        cursor.executemany(insert_into_gene_autocomplete_table, sample_data)
        cursor.close()
        self.db_connection.conn.commit()

    def prepare_test_data_success_case_limited_data(self):
        sample_data = [
            ('homo_sapiens', 'BRCA1'),
            ('homo_sapiens', 'BRCA2'),
            ('homo_sapiens', 'BRCA3'),
            ('homo_sapiens', 'BRCA4'),
        ]
        cursor = self.db_connection.conn.cursor()
        cursor.executemany(insert_into_gene_autocomplete_table, sample_data)
        cursor.close()
        self.db_connection.conn.commit()

    def assert_existing_table_data(self):
        cursor = self.db_connection.conn.cursor()
        return cursor.execute(select_all_from_gene_autocomplete_table).fetchall()
