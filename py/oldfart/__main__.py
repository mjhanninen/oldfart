import os
import socketserver

import oldfart.handler
import oldfart.make

makefile = 'Makefile'
project_dir = os.path.abspath('example')
server_dir = os.path.join(project_dir, 'build', 'dist')
port = 8000

# NB: Enforce local loopback interface
host = '127.0.0.1'

maker = oldfart.make.Maker(project_dir, makefile)

Handler = oldfart.handler.make_http_request_handler_class('MakerHTTP', maker)

if not os.path.exists(server_dir):
    os.makedirs(server_dir)
os.chdir(server_dir)

httpd = socketserver.TCPServer((host, port), Handler)

print('Serving "{:s}" through {:s}:{:d}'.format(server_dir, host, port))

httpd.serve_forever()
