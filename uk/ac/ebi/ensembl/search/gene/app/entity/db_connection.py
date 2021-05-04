import logging

from uk.ac.ebi.ensembl.search.gene.app.util.db_utility import load_credential, get_mysql_database_connection
from uk.ac.ebi.ensembl.search.gene.app.util.properties import test_ensembl_db_config_path

# create logger
logger = logging.getLogger('db-connection')
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)


class DBConnection:

    def __init__(self):
        self.db_credentials = load_credential(test_ensembl_db_config_path)
        self.db_connection = get_mysql_database_connection(self.db_credentials)

    def fetch_db_result(self, sql, *args):
        try:
            with self.db_connection.cursor() as cursor:
                if len(args) != 0:
                    cursor.execute(sql, args)
                else:
                    cursor.execute(sql)
            return cursor.fetchall()
        except Exception as expectedException:
            logger.exception(expectedException)
            raise Exception('Error while fetching data from database - ' + str(expectedException))

    def __del__(self):
        self.db_connection.close()
