# -*- coding: utf-8 -*-

"""
Functions for sending messages to log file

@author: Lises team
@contact: zhidkovseva@gmail.com
@license: The MIT license

Copyright (C) 2015
"""

import logging

# Set logging file
logging.basicConfig(filename='bot_log.log',level=logging.INFO)


def info_log_message(message):
    logging.info(message)


def warning_log_message(message):
    logging.warning(message)


def error_log_message(message):
    logging.error(message)


def critical_log_message(message):
    logging.critical(message)