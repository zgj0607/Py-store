# -*- coding: utf-8 -*-

from tornado.options import define, parse_command_line, options
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from Common.Urls import route

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

def run_tornado(ui):
    settings = {
        # 'template_path' : os.path.join(os.path.dirname(__file__),"templates"),
        # 'static_path' : os.path.join(os.path.dirname(__file__),"static"),
        # 'cookie_secret':"2379874hsdhf0234990sdhsaiuofyasop977djdj",
    }

    # route.append((r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))

    define("port", default=15775, help="run for the backend", type="int")
    parse_command_line()
    app = Application(
        handlers=route,
        **settings
    )

    http_server = HTTPServer(app)
    try:
        http_server.listen(options.port)
        IOLoop.instance().start()
    except Exception as e:
        print(e)
        ui.close()
