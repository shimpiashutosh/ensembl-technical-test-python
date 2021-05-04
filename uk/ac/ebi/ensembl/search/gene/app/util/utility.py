from werkzeug.exceptions import BadRequest


def is_valid_string(string):
    if not (string and not string.isspace()):
        raise BadRequest('Argument {str} should not contain only white spaces or should not be empty'.format(str=string))
