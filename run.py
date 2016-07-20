#!venv/bin/python
from app import app
from app.websocket import WSHandler
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler
import tornado.ioloop

tr = WSGIContainer(app)

application = Application([
    (r'/ws', WSHandler),
    (r".*", FallbackHandler, dict(fallback=tr)),
])

application.listen(9090)
tornado.ioloop.IOLoop.instance().start()
