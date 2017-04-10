# -*- encoding: utf-8 -*-

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class WSHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        self.write_message("Welcome to websocket")

    def on_message(self, message):
        self.write_message(u'Your message is: ' + message)

    def on_close(self):
        pass


class App(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/ws', WSHandler),
        ]

        settings = {
            "template_path": "."
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    ws_app = App()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
