import socketserver

import oldfart.handler
import oldfart.make

PORT = 8000

maker = oldfart.make.Maker('.')

Handler = oldfart.handler.make_http_request_handler_class('MakerHTTP', maker)

# NB: Enforce local loopback interface
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

httpd.serve_forever()
