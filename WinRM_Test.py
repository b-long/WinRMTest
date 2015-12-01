#!/usr/bin/env python

# Based on https://github.com/diyan/pywinrm
import winrm
import logging
import os

# create logger with 'winrm_test'
logger = logging.getLogger('winrm_test')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

host_with_winrm = os.environ["test_host"]
u = os.environ["test_u"]
p = os.environ["test_p"]

logger.info("Attempting to connect to WinRM host at %s", host_with_winrm)
logger.info("Will attempt authentication using u:'%s', p:'%s'", u, p)
s = winrm.Session(host_with_winrm, auth=(u, p))

def run_remote_command(session, cmd, options):
    result = session.run_cmd(cmd, options)
    logger.info("WinRM is connected")
    logger.info("Result status code :<<<\n%s\n>>>", result.status_code)
    logger.info("Result STDOUT :<<<\n%s\n>>>", result.std_out)
    logger.info("Result STDERR :<<<\n%s\n>>>", result.std_err)

run_remote_command(s, 'ipconfig', ['/all'])
run_remote_command(s, 'java', ['-version'])
