import os
import socketserver

import oldfart.handler
import oldfart.make

makefile = 'Makefile'
project_dir = os.path.abspath('example')
server_dir = os.path.join(project_dir, 'build', 'dist')
port = 8000

maker = oldfart.make.Maker(project_dir, makefile)

Handler = oldfart.handler.make_http_request_handler_class('MakerHTTP', maker)

if not os.path.exists(server_dir):
    os.makedirs(server_dir)
os.chdir(server_dir)

# NB: Enforce local loopback interface
httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)

httpd.serve_forever()
