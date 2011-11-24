from tornado.web import Application
from tornado.options import options

from urls import urlpatterns 


class TornadoApplication(Application):
    """Application class initilazid one time. """

    def __init__(self):
        handlers = urlpatterns
        settings = {}
        if options.debug:
            settings['debug']  = True
        super(TornadoApplication, self).__init__(handlers, **settings)
