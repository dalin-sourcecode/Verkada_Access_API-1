import logging
import os
from datetime import datetime

def setup_logger(name='verkada_api', log_level=logging.INFO):
	"""
	Set up a logger with file and console handlers.
	
	Args:
		name (str): Logger name
		log_level: Logging level (default: INFO)
	
	Returns:
		logging.Logger: Configured logger instance
	"""
	#############################################

	# Create logs directory if it doesn't exist
	log_dir = 'logs'
	if not os.path.exists(log_dir):
		os.makedirs(log_dir)

	#############################################

	# Create logger
	logger = logging.getLogger(name)

	logger.setLevel(log_level)

	#############################################

	# Clear existing handlers to avoid duplicates
	logger.handlers.clear()

	#############################################

	# Create formatters
	detailed_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s')

	simple_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

	#############################################
	
	# File handler for detailed logging
	today = datetime.now().strftime('%Y-%m-%d')

	file_handler = logging.FileHandler(os.path.join(log_dir, f'verkada_api_{today}.log'), encoding='utf-8')

	file_handler.setLevel(logging.DEBUG)

	file_handler.setFormatter(detailed_formatter)

	#############################################

	# Console handler for user-friendly output
	console_handler = logging.StreamHandler()

	console_handler.setLevel(log_level)

	console_handler.setFormatter(simple_formatter)
	
	# Add handlers to logger
	logger.addHandler(file_handler)

	logger.addHandler(console_handler)
	
	return logger


#############################################

def get_logger(name='verkada_api'):
	"""
	Get an existing logger or create a new one.
	
	Args:
		name (str): Logger name
	
	Returns:
		logging.Logger: Logger instance
	"""
	logger = logging.getLogger(name)

	if not logger.handlers:

		logger = setup_logger(name)

	return logger


