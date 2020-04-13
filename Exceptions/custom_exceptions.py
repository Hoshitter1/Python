from http import HTTPStatus
import json
from datetime import datetime


class BaseAPIError(Exception):
    """Any kinds of errors in API inherits this class"""


class APIError(BaseAPIError):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_msg = 'API exception occurred!'
    user_error_msg = 'We are sorry! An unexpected error occurred. ' \
                     'Please contact with XXX directly.'

    def __init__(self, *args, user_error_msg=None):
        if args:
            self.internal_error_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_error_msg)

        if user_error_msg is not None:
            self.user_error_msg = user_error_msg

    def to_json(self):
        err_objects = {'status': self.http_status, 'message': self.user_error_msg}
        return json.dumps(err_objects)

    def log(self):
        exception = {
            'type': type(self).__name__,
            'status': self.http_status,
            'message': self.args[0] if self.args else self.internal_error_msg,
            'extra args': self.args[1:]
        }
        print(
            f'Exception:[time]{datetime.utcnow().isoformat()}\n'
            f'exception: {exception}'
        )


class ApplicationError(APIError):
    """Indicates an applilcation error (not error caused by an user)"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_msg = 'application error occurred'
    user_error_msg = 'We are sorry! An unexpected error occurred. '


class DBError(APIError):
    """Database error """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_msg = 'database error occurred'
    user_error_msg = 'We are sorry! An unexpected error occurred. '


class ClientError(APIError):
    """ClientError error """
    http_status = HTTPStatus.BAD_REQUEST
    internal_error_msg = 'client submitted bad request'
    user_error_msg = "Are you Billie Eilish? you're the bad guy"


if __name__ == '__main__':
    try:
        raise ClientError('whaaaaat?','aa')
    except ClientError as e:
        e.log()
        print(e.to_json())
