import http.server
import os

import oldfart.make


__all__ = ['make_http_request_handler_class']


def _send_head(self):
    path = self.translate_path(self.path)
    target = os.path.relpath(path, os.getcwd())
    if not os.path.isdir(path):
        retval, output = self.maker.make(target)
        if retval == oldfart.make.FAILURE:
            self.send_error(500, 'Could not generate resource')
    return super(self.__class__, self).send_head()

def make_http_request_handler_class(name, maker):
    cls = type(name, (http.server.SimpleHTTPRequestHandler,), {
        'maker': maker,
        'send_head': _send_head
    })
    return cls