from flask_restful import reqparse


def build_arg_parser():
    parser = reqparse.RequestParser()  # initialize

    parser.add_argument('query', required=True)  # add args
    parser.add_argument('species', required=True)
    parser.add_argument('limit', required=True)

    return parser.parse_args()  # parse arguments to dictionary
