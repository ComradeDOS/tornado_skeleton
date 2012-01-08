import os

from tornado.web import Application
from tornado.options import options

from urls import urlpatterns 


class TornadoApplication(Application):
    """Application class initilazid one time."""

    def __init__(self):
        handlers = urlpatterns
        settings = {}
        if options.debug:
            settings['debug']  = True
        if options.static_path and os.path.exists(
                os.path.abspath(options.static_path)):
            settings['static_path'] = os.path.abspath(options.static_path)
        super(TornadoApplication, self).__init__(handlers, **settings)
