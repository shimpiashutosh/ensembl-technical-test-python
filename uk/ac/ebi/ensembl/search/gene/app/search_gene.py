import logging

from flask import Flask, Response, jsonify
from flask_restful import Api
from werkzeug.exceptions import BadRequest

from uk.ac.ebi.ensembl.search.gene.app.entity.db_connection import DBConnection
from uk.ac.ebi.ensembl.search.gene.app.parser.arg_parser import build_arg_parser
from uk.ac.ebi.ensembl.search.gene.app.util.sql_queries import get_gene_sql
from uk.ac.ebi.ensembl.search.gene.app.util.utility import is_valid_string

# create logger
logger = logging.getLogger('search-gene')
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)

app = Flask(__name__)
api = Api(app)

db_connection = DBConnection()


@app.route("/gene-suggestions")
def search_gene():
    try:
        query, species, limit = get_request_arg()
        gene_sql = get_gene_sql(query, species, limit)
        result_set = db_connection.fetch_db_result(gene_sql)
        return build_success_response(result_set)
    except (BadRequest, ValueError) as exp:
        logger.error(str(exp))
        return build_error_response("Bad request", 400)
    except Exception as exp:
        logger.error(str(exp))
        return build_error_response("Internal Server Error", 500)


def get_request_arg():
    args = build_arg_parser()

    query = args['query']
    species = args['species']
    limit = args['limit']

    is_valid_string(query)
    is_valid_string(species)
    int(limit)

    return query, species, limit


def build_success_response(result_set):
    if result_set is None or len(result_set) == 0:
        return build_error_response("Data not found", 404)

    payload = []
    for result in result_set:
        payload.append(result[0])
    return jsonify(payload)


def build_error_response(error_msg, http_status_code):
    return Response('{"message": "' + error_msg + '"}', status=http_status_code, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
