import logging
import os

# Globally set desired log levels for various modules
LOG_LEVELS = {
None: os.environ.get('DEFAULT_LOGLEVEL', logging.INFO),
'librato': logging.WARN,
'jobs': logging.INFO,
'test' : logging.WARN,
'test.test' : logging.INFO
}

for scope, level in LOG_LEVELS.items():
  logging.getLogger(scope).setLevel(level)

from google.appengine.api import logservice
logservice.AUTOFLUSH_ENABLED = True
logservice.AUTOFLUSH_EVERY_SECONDS = None
logservice.AUTOFLUSH_EVERY_BYTES = None
logservice.AUTOFLUSH_EVERY_LINES = 1
