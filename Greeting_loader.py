import datetime
from google.appengine.ext import db
from google.appengine.tools import bulkloader

class Greeting(db.Model):
  content = db.StringProperty(multiline=True)
  name = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)

class GreetingLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'Greeting',
                               [('name', str),
                                ('content', str),
                                ('publication_date',
                                 lambda x: datetime.datetime.strptime(x, '%m/%d/%Y').date()),
                               ])

loaders = [GreetingLoader]