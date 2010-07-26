from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template

from google.appengine.ext import db
from google.appengine.api import users

class Greeting(db.Model):
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  name = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class Del(webapp.RequestHandler):
  def get(self):
    q = db.GqlQuery("SELECT * FROM Greeting")
    results = q.fetch(10)
    for result in results:
      result.delete()

class Add(webapp.RequestHandler):
  def post(self):
    greeting = Greeting()

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.name = self.request.get('name')
    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/')

class Index(webapp.RequestHandler):
  def get(self):
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
      url = users.create_logout_url(self.request.uri)
      url_linktext = 'Logout'
    else:
      url = users.create_login_url(self.request.uri)
      url_linktext = 'Login'

    template_values = {
      'greetings': greetings,
      'url': url,
      'url_linktext': url_linktext,
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
  ('/', Index),
  ('/del', Del),
  ('/add', Add)
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()