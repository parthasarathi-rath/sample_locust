from datetime import datetime
import os
import logging
print(os.path.dirname(__file__))
curr_time = datetime.now().strftime("%H-%M-%S-%m%d%Y")
file_name = curr_time + ".log"
log_file = os.path.join(os.path.dirname(__file__), "logs", file_name)
print(log_file)
logging.debug
