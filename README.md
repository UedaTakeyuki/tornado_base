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

Also, a each tornado handlers is provided a same global dictionaly variable **tb_global** which can share for server global status.

### Structure
1. **TB_handler_classes**:  TB handler must have a module global variable **TB_handler_classes** which is a list of class name of tornado application handlers in this file. This is used by tornado_base.
2. **route**: Each tornado application hander class must have a class variable **route** for route definition. This is used by tornado base.

A tipical TB handler is as follows:

```python:
import tornado.websocket           '''in case include tornado websocket handler'''
import tornado.web                 '''in case include tornado request handler'''
from tornado import gen            '''in case to use gen'''
from tornado.log import app_log    '''in case to use tornado logging'''

''' 1. TB_handler_classes '''
TB_handler_classes = ["RS_WebPortalPageHander", "RS_WebCommandPageHandler"]

class RS_WebPortalPageHander(tornado.web.RequestHandler):
    ''' 2. route '''
    route = "/"
    def get(self):
        self.render('index.html', connections=connections)

class RS_WebCommandPageHandler(tornado.web.RequestHandler):
    ''' *** 2. route *** '''
    route = "/command"
    def get(self):
```

 ## options
Following options are available both command line and config file.

 ```
python tornado_base.py --help
Usage: tornado_base.py [OPTIONS]

Options:

  --help                           show this help information

/home/pi/.local/lib/python2.7/site-packages/tornado/log.py options:

  --log-file-max-size              max size of log files before rollover
                                   (default 100000000)
  --log-file-num-backups           number of log files to keep (default 10)
  --log-file-prefix=PATH           Path prefix for log files. Note that if you
                                   are running multiple tornado processes,
                                   log_file_prefix must be different for each
                                   of them (e.g. include the port number)
  --log-rotate-interval            The interval value of timed rotating
                                   (default 1)
  --log-rotate-mode                The mode of rotating files(time or size)
                                   (default size)
  --log-rotate-when                specify the type of TimedRotatingFileHandler
                                   interval other options:('S', 'M', 'H', 'D',
                                   'W0'-'W6') (default midnight)
  --log-to-stderr                  Send log output to stderr (colorized if
                                   possible). By default use stderr if
                                   --log_file_prefix is not set and no other
                                   logging is configured.
  --logging=debug|info|warning|error|none 
                                   Set the Python log level. If 'none', tornado
                                   won't touch the logging configuration.
                                   (default info)

tornado_base.py options:

  --additional-module-paths=path1, path2... 
                                   list of module paths
  --cert-file                      cert file name for running with ssl (default
                                   cert.pem)
  --config-file                    config file path
  --data-dir                       cert file path for running with ssl
  --port                           listening port (default 8888)
  --privkey-file                   privkey file name for running with ssl
                                   (default privkey.pem)
  --protocol                       ws: or wss:(default) (default wss:)
  --static-path                    [mandatory] handler class name of rhizome
                                   (default sample_handlers/static)
  --tb-handlers=handler1, handler2... 
                                   list of Tornado Base handler files
  --templates-path                 [mandatory] handler class name of rhizome
                                   (default sample_handlers/templates)
 ```

A config-file must be a python file which is consist of **option=value**. A sample is available as [this]()

The priority of option is as follows:

1. config file 
