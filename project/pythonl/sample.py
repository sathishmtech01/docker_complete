import logging

log_format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
log_activity = "activity_log"
logging.basicConfig(filename="sample_container1.log", level=logging.DEBUG, format=log_format)
# log data
logger = logging.getLogger(log_activity)
logger.setLevel(logging.DEBUG)

# "application" code
logger.debug("debug message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

if __name__ == '__main__':
    pass