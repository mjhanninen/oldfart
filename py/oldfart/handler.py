import http.server
import os

import oldfart.make


__all__ = ['make_http_request_handler_class']


# The idea here is to modify the request handling by intercepting the
# `send_head` call which is combines the common bits of GET and HEAD commands
# and, more importantly, is the first method in the request handling process
# that accesses the file system. Try to generate the resource to the file
# system just before the parent, SimpleHTTPRequestHandle, needs it and we're
# done.

def _send_head(self):
    # FIXME: We die here if the directory doesn't exist ('make clean'
    # anyone?). All fixes seem ugly. Think about it.
    path = self.translate_path(self.path)
    target = os.path.relpath(path, self.maker.project_dir)
    if not os.path.isdir(path):
        retval, output = self.maker.make(target)
        if retval == oldfart.make.FAILURE:
            self.log_error('Building resource failed:\n%s', output)
            self.send_error(500, 'Could not generate resource')
            return None
        elif retval == oldfart.make.NO_RULE:
            self.log_message('No rule for building the resource')
    return super(self.__class__, self).send_head()


def make_http_request_handler_class(name, maker):
    cls = type(name, (http.server.SimpleHTTPRequestHandler,), {
        'maker': maker,
        'send_head': _send_head
    })
    return cls
