#-*- coding:utf-8 -*-
# Copy Right Takeyuki UEDA  © 2018 - All rights reserved.

#protocol = "wss:"
protocol = "ws:"

data_dir = "/etc/letsencrypt/live/titurel.uedasoft.com/"
additional_module_path    = ["sample_handlers"] 
rhizosperehandlers    = ["sample"]

log_file_prefix = "/var/log/tornado_base"
logging = "debug"