#-*- coding:utf-8 -*-
# Copy Right Takeyuki UEDA  © 2019 - All rights reserved.

#protocol = "wss:"
protocol = "ws:"

data_dir = "/etc/letsencrypt/live/.com/"
additional_module_paths    = ["sample_handlers"]
tb_handlers    = ["ws_exchange", "sample"]
templates_path = "sample_handlers/templates"

log_file_prefix = "/var/log/tornado_base/tb.log"
logging = "debug"
