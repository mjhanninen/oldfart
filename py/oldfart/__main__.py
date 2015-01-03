import socketserver

import oldfart.handler

PORT = 8000

Handler = oldfart.handler.MakerHTTPRequestHandler

# NB: Enforce local loopback interface
httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)

httpd.serve_forever()
