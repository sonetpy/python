import logging
import logging.config
logging.config.fileConfig('temp.conf')
# create logger
logger = logging.getLogger('Abhinav')
 
# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')