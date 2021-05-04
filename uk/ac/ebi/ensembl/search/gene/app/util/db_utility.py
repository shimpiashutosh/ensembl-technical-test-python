import json
import logging
import os
from getpass import getpass

import pymysql

# create logger
logger = logging.getLogger('db-utility')
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)


def load_credential(db_credentials_path):
    root_dir = os.path.split(os.path.realpath(__file__))[0]
    config_file_path = os.path.join(root_dir, db_credentials_path)
    expanded_filepath = os.path.expanduser(config_file_path)

    if not os.path.exists(expanded_filepath):
        raise Exception('Credentials file {} does not exist'.format(expanded_filepath))

    try:
        with open(expanded_filepath) as f:
            cfg = json.load(f)
        if 'host' not in cfg:
            cfg['host'] = input('Enter database host :')
        if 'port' not in cfg:
            cfg['port'] = input('Enter database port :')
        if 'database' not in cfg:
            cfg['database'] = input('Enter database name :')
        if 'username' not in cfg:
            cfg['username'] = input('Enter database username :')
        if 'password' not in cfg:
            cfg['password'] = getpass('Enter database password for {} : '.format(cfg['username']))
    except ValueError:
        logger.exception(ValueError)
        raise Exception('Error while processing database configuration - ' + str(ValueError))

    return cfg['host'], cfg['port'], cfg.get('database'), cfg['username'], cfg.get('password')


def get_mysql_database_connection(credentials):
    (host, port, database, username, password) = credentials
    return pymysql.connect(host=host, port=port, db=database, user=username, password=password)
