# -*- coding: utf-8 -*-
import logging

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
from tornado.web import Application

from Common.Urls import route

logger = logging.getLogger(__name__)


def run_tornado(ui):
    settings = {}

    define("port", default=15775, help="run for the backend", type="int")
    parse_command_line()
    app = Application(
        handlers=route,
        **settings
    )

    http_server = HTTPServer(app)
    try:
        logger.info('Web server 启动中...')
        http_server.listen(options.port)
        logger.info('Web server 已启动，监听端口：' + str(options.port))
        IOLoop.instance().start()
    except Exception as e:
        logger.error(e.__str__())
        ui.close()
