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
TB_handler_classes = ["RS_WebHander1", "RS_WebHander2"]


class RS_WebHander1(tornado.web.RequestHandler):
    route = "/"
    def get(self):
        connections = [1,2,3]
        self.render('index.html')

class RS_WebHander2(tornado.web.RequestHandler):
    route = "/(.*)"
    def get(self,name):
        self.render('hello.html', name=name)

