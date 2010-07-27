# -*- coding: utf-8 -*-
#!/usr/bin/env python

import cgi
import os
import time
import datetime

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

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
    categorys= [ {'name':'stgj', 'value':'系统工具'},
              {'name':'hlwyy', 'value':'互联网应用'},
              {'name':'aqfh', 'value':'安全防护'},
              {'name':'dmt', 'value':'多媒体'},
              {'name':'zmzt', 'value':'桌面主题'},
              {'name':'sygj', 'value':'实用工具'},
              {'name':'bgxx', 'value':'办公学习'},
              {'name':'dtdh', 'value':'地图导航'},
              {'name':'dzs', 'value':'电子书'},
              {'name':'gjbd', 'value':'固件补丁'}
            ]

    hao123category= [
              {'name':'sq', 'value':'社 区'},
              {'name':'yy', 'value':'音 乐'},
              {'name':'cj', 'value':'财 经'},
              {'name':'gw', 'value':'购 物'},
              {'name':'xs', 'value':'小 说'},
              {'name':'yx', 'value':'游 戏'},
              {'name':'kj', 'value':'空 间'},
              {'name':'wy', 'value':'网 游'},
              {'name':'qc', 'value':'汽 车'},
              {'name':'sp', 'value':'视 频'},
              {'name':'ty', 'value':'体 育'},
            ]
            
    hao123category2= [
              {'name':'js', 'value':'军 事'},
              {'name':'jy', 'value':'交 友'},
              {'name':'dn', 'value':'电 脑'},
              {'name':'xw', 'value':'新 闻'},
              {'name':'lt', 'value':'聊 天'},
              {'name':'nx', 'value':'女 性'},
              {'name':'xz', 'value':'星 座'},
              {'name':'dm', 'value':'动 漫'},
              {'name':'ly', 'value':'旅 游'},
              {'name':'mx', 'value':'明 星'},
              {'name':'ss', 'value':'时 尚'},
            ]
            
    
    str = ''
    for i in range(0,len(hao123category)):
        str = str + '<tr><td><a href="android123?category='+hao123category[i]['name']+'">'+hao123category[i]['value']+'</a></td><td>&nbsp;&nbsp;&nbsp;</td><td><a href="android123?category='+hao123category2[i]['name']+'">'+hao123category2[i]['value']+'</a></td></tr>'
    greetings_query = Greeting.all().order('-date')
    greetings = greetings_query.fetch(10)

    template_values = {
      'categorys': categorys,
      'str': str,
      }

    path = os.path.join(os.path.dirname(__file__), 'index.html')
    self.response.out.write(template.render(path, template_values))

class AndroidSoftware(db.Model):
  title = db.StringProperty()
  desc = db.StringProperty()
  category = db.StringProperty()
  type = db.StringProperty()
  size = db.StringProperty()
  updatedate = db.DateProperty(auto_now_add=True)
  name = db.StringProperty()
  numbers = db.StringProperty()
  imgurl = db.StringProperty()
  link = db.StringProperty()
  downloadurl = db.StringProperty()
  downloadpageurl = db.StringProperty()
  downloadfileurl = db.StringProperty()
  filename = db.StringProperty()
  filenamefixed = db.StringProperty()

class Software(webapp.RequestHandler):
  def get(self):
    categorys= {'stgj':'系统工具',
              'hlwyy':'互联网应用',
              'aqfh':'安全防护',
              'dmt':'多媒体',
              'zmzt':'桌面主题',
              'sygj':'实用工具',
              'bgxx':'办公学习',
              'dtdh':'地图导航',
              'dzs':'电子书',
              'gjbd':'固件补丁'
            }

    q = db.GqlQuery("SELECT * FROM AndroidSoftware WHERE category='"+categorys[cgi.escape(self.request.get('category'))].decode('utf-8')+"'")
    #q = db.GqlQuery("SELECT * FROM AndroidSoftware WHERE category='"+u'系统工具'+"'")
    results = q.fetch(500)
    
    #error = categorys[cgi.escape(self.request.get('category'))]
    
    template_values = {
      'softwares': results,
      'category': categorys[cgi.escape(self.request.get('category'))],
      }

    path = os.path.join(os.path.dirname(__file__), 'software.html')
    self.response.out.write(template.render(path, template_values))

class Hao123(db.Model):
  category = db.StringProperty()
  type = db.StringProperty()
  htmltext = db.StringProperty()
  htmllink = db.StringProperty()

class Android123(webapp.RequestHandler):
  def get(self):
    hao123category= {
              'sq':'社 区',
              'yy':'音 乐',
              'cj':'财 经',
              'gw':'购 物',
              'xs':'小 说',
              'yx':'游 戏',
              'kj':'空 间',
              'wy':'网 游',
              'qc':'汽 车',
              'sp':'视 频',
              'ty':'体 育',
              'js':'军 事',
              'jy':'交 友',
              'dn':'电 脑',
              'xw':'新 闻',
              'lt':'聊 天',
              'nx':'女 性',
              'xz':'星 座',
              'dm':'动 漫',
              'ly':'旅 游',
              'mx':'明 星',
              'ss':'时 尚',
            }
            
    q = db.GqlQuery("SELECT * FROM Hao123 WHERE category='"+hao123category[cgi.escape(self.request.get('category'))].decode('utf-8')+"'")
    results = q.fetch(500)
    
    template_values = {
      'android123': results,
      'category': hao123category[cgi.escape(self.request.get('category'))],
      }

    path = os.path.join(os.path.dirname(__file__), 'android123.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
  ('/', Index),
  ('/del', Del),
  ('/add', Add),
  ('/software', Software),
  ('/android123', Android123),
], debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()