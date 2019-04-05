# tornado_base
A framework of tornado for modularity.

## Purpose
* Modularity  of Tornado Application handler file.
* Reusability of option definition

## Architecture
* **tornado_base**: parse options, read **TB handler**s, compose appropricate tornado App class, then run tornado server.  
* **TB handler**: Application definition module files

## TB handler
**TB handler** is a python module file which is consist of tornado Request handlers or/and tornado Websocket handlers. Each tornado handlers in TB handler are composed to a tornado application handler by/for **tornado_base**.

One of an advantage of TB handler is that: tornado handlers in the same TB handler file can share the **same module global**. You can gather related tornado handler modules on the same TB handler file to share glovals, and separate non-related tornado handlers into each TB handler files as your necesity.

Also, a each tornado handlers is provided a same global dictionaly variable **tb_grobal** which can share for server global status.

### Structure
* TB handler must have a module global variable **TB_handler_classes** which is a list of class name of tornado application handlers in this file. This is used by tornado_base.
* Each tornado application hander class must have a class variable **route** for route definition. This is used by tornado base.

A tipical TB handler is as follows:

```python:
import tornado.websocket           '''in case include tornado websocket handler'''
import tornado.web                 '''in case include tornado request handler'''
from tornado import gen            '''in case to use gen'''
from tornado.log import app_log    '''in case to use tornado logging'''

''' 
TB_handler_classes:

The global list of tornado application handler class name in this file.
The class in this list is gathered and composed for tornado application by tornado_base
'''
TB_handler_classes = ["RS_WebPortalPageHander", "RS_WebCommandPageHandler"]

class RS_WebPortalPageHander(tornado.web.RequestHandler):
    ''' 
    route:    
    The route definition, parsed and set by tornado_base
    '''
    route = "/"
    def get(self):
        self.render('index.html', connections=connections)

class RS_WebCommandPageHandler(tornado.web.RequestHandler):
    ''' 
    route:    
    The route definition, parsed and set by tornado_base
    '''
    route = "/command"
    def get(self):
```
