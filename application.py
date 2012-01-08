import os

from tornado.web import Application
from tornado.options import options

from urls import urlpatterns 


class TornadoApplication(Application):
    """Application class initilazid one time."""

    def __init__(self):
        handlers = urlpatterns
        settings = {}
        settings['debug'] = options.debug

        if options.static_path and os.path.exists(
                os.path.abspath(options.static_path)):
            settings['static_path'] = os.path.abspath(options.static_path)

        settings['static_url_prefix'] = options.static_url_prefix

        if options.template_path and os.path.exists(
                os.path.abspath(options.template_path)):
            settings['template_path'] = os.path.abspath(options.template_path)

        settings['gzip'] = options.gzip

        super(TornadoApplication, self).__init__(handlers, **settings)
