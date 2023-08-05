import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
log_file_path = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(filename=log_file_path,
                    level=logging.INFO, format=logging_str)

handler = [
    logging.StreamHandler(sys.stdout),
    logging.FileHandler(log_file_path)
]

logger = logging.getLogger('chicken_disease_classification logger')
