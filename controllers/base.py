from tornado.web import RequestHandler

class BaseRequestHandler(RequestHandler):

    def get(self):
        self.write('Hello, World!')
