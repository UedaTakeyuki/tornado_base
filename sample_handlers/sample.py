#-*- coding:utf-8 -*-
# Copy Right Takeyuki UEDA  © 2018 -

import tornado.websocket
import tornado.web
from tornado import gen

from tornado.log import app_log

'''
A global variable of dictionaly "connections" should be added at outside of this module,
 and share between rhizosphere main function.
'''

type = "RS_cdpair_and_connections_shares"
TB_handler_classes = ["RS_WebPortalPageHander", "RS_WebCommandPageHandler"]


class RS_WebPortalPageHander(tornado.web.RequestHandler):
    route = "/"
    def get(self):
        connections = [1,2,3]
        self.render('index.html', connections="connections")

class RS_WebCommandPageHandler(tornado.web.RequestHandler):
    route = "/command"
    def get(self):
        try:
            id      = self.get_argument('id')
            cmd_str = self.get_argument('cmd_str')
        except tornado.web.MissingArgumentError:
            pass

        self.render('client.html', connections=connections, id=id)
