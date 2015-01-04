import argparse
import os
import socketserver

import oldfart.handler
import oldfart.make

default_project_dir = os.path.abspath('.')

default_makefile_path = 'Makefile'

default_server_dir = default_project_dir

default_port = 8000

parser = argparse.ArgumentParser(description='Serve make(1) targets.')

opt = parser.add_argument

opt('--port', metavar='PORT', dest='port', type=int, default=default_port,
    help='Specify alternate port')

opt('--serve-from', metavar='DIR', dest='server_dir', type=str,
    default=default_server_dir, help='Serve resources from directory DIR')

opt('--project-dir', metavar='DIR', dest='project_dir', type=str,
    default=default_project_dir,
    help='Project is located in DIR. Make(1) is executed in the context of '
         'this directory')

opt('--makefile', metavar='PATH', dest='makefile_path', type=str,
    default=default_makefile_path,
    help='Path to Makefile relative to the project directory')

args = parser.parse_args()

# NB: Enforce local loopback interface
host = '127.0.0.1'

maker = oldfart.make.Maker(args.project_dir, args.makefile_path)

Handler = oldfart.handler.make_http_request_handler_class('MakerHTTP', maker)

if not os.path.exists(args.server_dir):
    os.makedirs(args.server_dir)
os.chdir(args.server_dir)

httpd = socketserver.TCPServer((host, args.port), Handler)

print('Serving "{:s}" through {:s}:{:d}'.format(args.server_dir, host,
                                                args.port))

httpd.serve_forever()
