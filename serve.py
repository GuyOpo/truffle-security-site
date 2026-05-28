#!/usr/bin/env python3
import http.server
import os

os.chdir('/Users/guyo/Desktop/truffle-website')
handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(('', 8765), handler) as httpd:
    print('Serving on port 8765')
    httpd.serve_forever()
