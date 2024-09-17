"""Exception classes"""

import logging
import traceback
import uuid

LOG = logging.getLogger(__name__)


def format_exception_response(exception):
    """Format exception response for web response JSON"""
    message = exception.message
    e = exception
    while e.__cause__:
        e = e.__cause__
        message += ' - ' + str(e)
    return {
        "error": message,
        "data": getattr(exception, 'data', None),
        "debug": traceback.format_tb(exception.__traceback__)
    }
    
class RootException(Exception):
    """Root exception class"""
    def __init__(self, message, data=None):
        self.id = str(uuid.uuid4())
        self.message = message
        self.data = data



