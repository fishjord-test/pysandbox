import webapp2

from google.appengine.ext import db
from google.appengine.api import users

class PushModel(db.Model):
    contents = db.TextProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class RequestLogger(webapp2.RequestHandler):
    def get(self):
        self.handle()

    def post(self):
        self.handle()

    def handle(self):
        data = PushModel(contents=str(self.request))
        data.put()
        self.response.status = 200

class RequestViewer(webapp2.RequestHandler):
    def get(self):
        q = PushModel.all()
        q.order('-created')
        self.response.headers['Content-Type'] = 'text/plain'
        for req in q.run():
            self.response.write('{0}\t{1}\t\n\n'.format(req.created, req.contents))

