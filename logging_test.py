import webapp2

import logging
import sys
import request_logger
import time

from google.appengine.api import logservice

from google.appengine.api import logservice
logservice.AUTOFLUSH_ENABLED = True
logservice.AUTOFLUSH_EVERY_SECONDS = None
logservice.AUTOFLUSH_EVERY_BYTES = None
logservice.AUTOFLUSH_EVERY_LINES = 1

class LoggingTest(webapp2.RequestHandler):
    def get(self):
        l1 = logging.getLogger("test");
        l2 = logging.getLogger("test.test");

        l1.critical("nohandler: test nohandler")
        l1.info("nohandler: test nohandler")
        l1.warn("nohandler: test nohandler")
        l1.critical("nohandler: test nohandler")
        l2.critical("stdouthandler: test handler")

        logging.getLogger(__name__).debug(__name__ + ": debug")
        logging.getLogger(__name__).critical(__name__ + ": critical")

        l1.critical("nohandler: test nohandler")
        l2.critical("stdouthandler: test handler")

        logservice.flush()

        logservice.AUTOFLUSH_ENABLED = True
        logservice.AUTOFLUSH_EVERY_SECONDS = None
        logservice.AUTOFLUSH_EVERY_BYTES = None
        logservice.AUTOFLUSH_EVERY_LINES = 1

        time.sleep(5)

        l1.critical("post sleep")
        l2.critical("post sleep")

        open("etc", "w")

        #t = [0] * 268435456

        l1.critical("post big alloc")
        l2.critical("post big alloc")

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

