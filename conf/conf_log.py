import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='logs/project.log'):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                'logs/project_logs.log', 
                maxBytes=5000000, 
                backupCount=5
            ),
            logging.StreamHandler()
        ],
        encoding="utf-8"
    )