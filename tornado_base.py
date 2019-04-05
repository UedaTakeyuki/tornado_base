#-*- coding:utf-8 -*-
# Copy Right Takeyuki UEDA  © 2019 - All rights reserved.
'''
Tornado Base:

A framework of tornado for modularity.
'''

import tornado.ioloop
import tornado.web
from tornado.options import define, options
import ssl
import os
import sys
import pprint
import importlib

tb_global = []

'''
   return: taple of (route, class) for tornado app constructor
'''
def get_handlerclass_and_route(module, classname):
    handlerclass = getattr(module, classname)
    return (handlerclass.route, handlerclass)

'''
   return: apphandler_list appended tornado handlers
'''
def append_tbhandler(apphandler_list, tb_handler):    
    global tb_global

    ''' import tb_handler '''
    mod = importlib.import_module(tb_handler)

    ''' add tb_global '''
    mod.tb_global = tb_global

    tb_handler_classes = getattr(mod, "TB_handler_classes")
    for handler_class_name in tb_handler_classes:
        apphandler_list.append(get_handlerclass_and_route(mod, handler_class_name))

    return apphandler_list

if __name__ == "__main__":
# options
    define("protocol",               default="wss:", help="ws: or wss:(default)")
    define("port",                   default=8888, help="listening port", type=int)    
    define("data_dir",               default="", help="cert file path for running with ssl")
    define("cert_file",              default="cert.pem", help="cert file name for running with ssl")
    define("privkey_file",           default="privkey.pem", help="privkey file name for running with ssl")
    define("config_file",            default="",         help="config file path")
    define("tb_handlers",            default="",         help="list of Tornado Base handler files",multiple=True, metavar="handler1, handler2...")
    define("additional_module_paths",default="",         help="list of module paths",multiple=True, metavar="path1, path2...")
    define("static_path",            default="sample_handlers/static",        help="[mandatory] handler class name of rhizome")
    define("templates_path",         default="sample_handlers/templates",     help="[mandatory] handler class name of rhizome")

    options.parse_command_line()

    '''
    The priority of Option file

    1. options.config_file
    2. ./config.py
    '''
    if options.config_file:
        options.parse_config_file(options.config_file, final=False)
    elif os.path.exists('./config.py'):
        options.parse_config_file('./config.py', final=False)

    '''
    command line is the first priority
    '''
    options.parse_command_line()

    # https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
    if options.additional_module_paths:
        [sys.path.append(x) for x in options.additional_module_paths]

# app
    BASE_DIR = os.path.dirname(__file__)

    app_params = {}
    app_params["handler"]       = []
    app_params["template_path"] = os.path.join(BASE_DIR, options.templates_path)
    app_params["static_path"]   = os.path.join(BASE_DIR, options.static_path)

    for tb_handler in options.tb_handlers:
        requesthandlers = append_tbhandler(app_params["handler"], tb_handler)
    print(app_params["handler"])

    app = tornado.web.Application(
        app_params["handler"], 
        template_path = app_params["template_path"],
        static_path   = app_params["static_path"],
    )

    if options.protocol == "ws:":
        http_server = tornado.httpserver.HTTPServer(app)
    else:
        ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        data_dir = options.data_dir
        ssl_ctx.load_cert_chain(os.path.join(data_dir, options.cert_file),
                                os.path.join(data_dir, options.privkey_file))
        http_server = tornado.httpserver.HTTPServer(app, ssl_options=ssl_ctx)

    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()