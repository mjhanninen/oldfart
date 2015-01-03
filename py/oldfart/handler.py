import http.server
import os

import oldfart.make


maker = oldfart.make.Maker('.')


class MakerHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    server_version = 'MakerHTTP/0.1'

    def send_head(self):
        path = self.translate_path(self.path)
        target = os.path.relpath(path, os.getcwd())
        if not os.path.isdir(path):
            retval, output = maker.make(target)
            if retval == oldfart.make.FAILURE:
                self.send_error(500, 'Could not generate resource')
        return super().send_head()
