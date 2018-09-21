#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
learning.py

A Python 3 tutorial from https://www.liaoxuefeng.com

Usage:

python3 learning.py
'''

# check #######################################################################

import sys
from datetime import datetime

CERT_EXPIRES = '2018-07-01'

def check_version():
    v = sys.version_info
    if v.major == 3 and v.minor >= 5:
        return
    print('Your current python is %d.%d. Please use Python 3.6.' % (v.major, v.minor))
    exit(1)

def check_cert():
    today = datetime.now().strftime('%Y-%m-%d')
    if today >= CERT_EXPIRES:
        print('This learning.py is expired. Please download a newer version.')
        exit(1)

check_version()
check_cert()

# start server ################################################################

import os, io, json, subprocess, tempfile, ssl
from urllib import parse
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler

EXEC = sys.executable
PORT = 39093
TEMP = tempfile.mkdtemp(suffix='_py', prefix='learn_python_')

HTML_INDEX = r'''
<html>
  <head><title>Learning Python</title></head>
  <body>
    <form method="post" action="/run">
      <textarea name="code" style="width:90%;height: 600px"></textarea>
      <p><button type="submit">Run</button></p>
    </form>
  </body>
</html>
'''

class LearningHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.close_connection = True
        if self.path != '/':
            return self.send_error(404)
        self._sendHttpHeader('text/html')
        self._sendHttpBody(HTML_INDEX)

    def do_POST(self):
        self.close_connection = True
        if self.path != '/run':
            return self.send_error(400)
        print('Prepare code...')
        body = self.rfile.read(int(self.headers['Content-length']))
        qs = parse.parse_qs(body.decode('utf-8'))
        if not 'code' in qs:
            return self.send_error(400)
        code = qs['code'][0]
        r = dict()
        try:
            fpath = write_py(get_name(), code)
            print('Execute: %s %s' % (EXEC, fpath))
            r['output'] = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
        except subprocess.CalledProcessError as e:
            r = dict(error='Exception', output=decode(e.output))
        except subprocess.TimeoutExpired as e:
            r = dict(error='Timeout', output='执行超时')
        except subprocess.CalledProcessError as e:
            r = dict(error='Error', output='执行错误')
        print('Execute done.')
        self._sendHttpHeader()
        self._sendHttpBody(r)

    def _sendHttpHeader(self, contentType='application/json'):
        origin = self.headers['Origin'] or 'https://www.liaoxuefeng.com'
        self.send_response(200)
        self.send_header('Content-Type', contentType)
        self.send_header('Access-Control-Allow-Origin', origin)
        self.send_header('Access-Control-Allow-Methods', 'GET,POST')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

    def _sendHttpBody(self, data):
        body = b''
        if isinstance(data, bytes):
            body = data
        elif isinstance(data, str):
            body = data.encode('utf-8', errors='ignore')
        else:
            body = json.dumps(data).encode('utf-8', errors='ignore')
        self.wfile.write(body)

def main():
    certfile = write_cert()
    httpd = HTTPServer(('127.0.0.1', PORT), LearningHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, server_side=True)
    print('Ready for Python code on port %d...' % PORT)
    print('Press Ctrl + C to exit...')
    httpd.serve_forever()

# functions ###################################################################

INDEX = 0

def get_name():
    global INDEX
    INDEX = INDEX + 1
    return 'test_%d' % INDEX

def write_py(name, code):
    fpath = os.path.join(TEMP, '%s.py' % name)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    print('Code wrote to: %s' % fpath)
    return fpath

def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

# certificate #################################################################

def write_cert():
    fpath = os.path.join(TEMP, 'local.liaoxuefeng.com.pem')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(CERT_DATA)
    return fpath


if __name__ == '__main__':
    main()
