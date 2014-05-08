import webapp2

import logging
import sys
import request_logger
import logging_test

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/log_test', logging_test.LoggingTest),
    ('/logger', request_logger.RequestLogger),
    ('/log_view', request_logger.RequestViewer),
], debug=True)
