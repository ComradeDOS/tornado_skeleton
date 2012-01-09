#!/bin/env python
import os
import logging

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options, parse_command_line,\
                            parse_config_file

from application import TornadoApplication as app


define('debug', type=bool, default=False,
       help='run application in debug mode (single thread, '
            'with autoreload module enabled)')
define('address', type=str, default='0.0.0.0',
       help='run application on given interface')
define('port', type=int, default=8000,
       help='run application on given port')

define('static_path', type=str, default='static',
       help='path to the static content')
define('static_url_prefix', type=str, default='/static/',
       help='url prefix for static content')

define('template_path', type=str, default='views',
       help='path to the directory with templates')

define('gzip', type=bool, default=False,
       help='use gzip compression for response')

define('certfile', type=str, default='', help='path to the certificate')
define('keyfile', type=str, default='', help='path to the keyfile')

log = logging.getLogger(__name__)

def main():
    if os.path.exists('settings.py'):
        parse_config_file('settings.py')
    parse_command_line()
    ssl_options = {}
    if (options.certfile and options.keyfile) and (os.path.exists(
            os.path.abspath(options.certfile)) and os.path.exists(
            os.path.abspath(options.keyfile))):
        ssl_options['certfile'] = os.path.abspath(options.certfile)
        ssl_options['keyfile'] = os.path.abspath(options.keyfile)
    server = HTTPServer(app(), ssl_options=ssl_options or None)
    if options.debug:
        options.address = '127.0.0.1'
        log.debug('Run application in debug mode on %s:%s.' % (options.address,
                                                               options.port))
        server.listen(options.port, options.address)
    else:
        log.debug('Run application in normal mode on %s:%s.' % (options.address,
                                                                options.port))
        server.bind(options.port, options.address)
        server.start(0)
    IOLoop.instance().start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.debug('Stop IOLoop instance.')
        IOLoop.instance().stop()
        log.debug('Freeing resources.')
        IOLoop.instance().close()
