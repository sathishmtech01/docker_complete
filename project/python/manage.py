#!/usr/bin/env python
import os
import sys
import logging

log_format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
log_activity = "activity_log"
logging.basicConfig(filename="sample_container_docker.log", level=logging.DEBUG, format=log_format)
# log data
logger = logging.getLogger(log_activity)
logger.setLevel(logging.DEBUG)

# "application" code
logger.debug("debug message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoapi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )from exc
    execute_from_command_line(sys.argv)
