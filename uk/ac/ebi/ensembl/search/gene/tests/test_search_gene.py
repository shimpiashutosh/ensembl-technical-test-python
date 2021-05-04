import unittest
from unittest import mock

from uk.ac.ebi.ensembl.search.gene.app.search_gene import app
from uk.ac.ebi.ensembl.search.gene.tests.util.db_connection_test import DBConnectionTest
from uk.ac.ebi.ensembl.search.gene.tests.util.prepare_test_data import PrepareTestData
from uk.ac.ebi.ensembl.search.gene.tests.util.sql_commands_test import create_gene_autocomplete_table, \
    drop_gene_autocomplete_table, truncate_gene_autocomplete_table

db_connection_test_obj = DBConnectionTest()
db_connection = db_connection_test_obj.conn

SUCCESS = 200
BAD_REQUEST = 400
DATA_NOT_FOUND = 404


@mock.patch("uk.ac.ebi.ensembl.search.gene.app.search_gene.db_connection", db_connection_test_obj)
class SearchGeneTest(unittest.TestCase):
    prepare_test_data = PrepareTestData(db_connection_test_obj)

    @classmethod
    def setUpClass(cls):
        db_connection.execute(create_gene_autocomplete_table)

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        db_connection.execute(truncate_gene_autocomplete_table)

    @classmethod
    def tearDownClass(cls):
        db_connection.execute(drop_gene_autocomplete_table)

    def test_when_call_search_gene_then_return_data_successfully(self):
        # Given: prepare test data
        SearchGeneTest.prepare_test_data.prepare_test_data_success_case()

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=brc&species=homo_sapiens&limit=2')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(['BRCA1', 'BRCA2'], response.get_json())
        self.assertEqual(SUCCESS, response.status_code)

    def test_when_call_search_gene_then_return_limited_data_successfully(self):
        # Given: check for any existing data
        existing_data = SearchGeneTest.prepare_test_data.assert_existing_table_data()
        self.assertEqual(0, len(existing_data))

        # prepare test data
        SearchGeneTest.prepare_test_data.prepare_test_data_success_case_limited_data()
        new_data = SearchGeneTest.prepare_test_data.assert_existing_table_data()
        self.assertIsNotNone(new_data)
        self.assertEqual(4, len(new_data))

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=brc&species=homo_sapiens&limit=3')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(['BRCA1', 'BRCA2', 'BRCA3'], response.get_json())
        self.assertEqual(200, response.status_code)

    def test_when_call_search_gene_then_return_data_not_found(self):
        # Given: nothing

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=test&species=test&limit=1')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(DATA_NOT_FOUND, response.status_code)

    def test_when_call_search_gene_then_return_bad_request_invalid_limit(self):
        # Given: nothing

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=test&species=test&limit=str')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(BAD_REQUEST, response.status_code)

    def test_when_call_search_gene_then_return_bad_request_empty_query(self):
        # Given: nothing

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=&species=test&limit=2')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(BAD_REQUEST, response.status_code)

    def test_when_call_search_gene_then_return_bad_request_empty_species(self):
        # Given: nothing

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=test&species&limit=2')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(BAD_REQUEST, response.status_code)

    def test_when_call_search_gene_then_return_bad_request_no_species_parameter(self):
        # Given: nothing

        # Test: API to be tested
        response = self.app.get('/gene-suggestions?query=test&limit=2')

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(BAD_REQUEST, response.status_code)


if __name__ == '__main__':
    unittest.main()
