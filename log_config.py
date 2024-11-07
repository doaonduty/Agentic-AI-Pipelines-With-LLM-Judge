import logging

# Create a logger
logger = logging.getLogger('log_flow')
logger.setLevel(logging.INFO)

# Create a file handler and a console handler
file_handler = logging.FileHandler('log.txt')
console_handler = logging.StreamHandler()

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)