import webapp2
import jinja2
import logging
import os
import urllib2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {
            'topic' : ''
        }

        template = jinja_environment.get_template('views/index.html')
        self.response.out.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
  def get(self):  
    template_values = {'topic' : self.request.get('topic')
    }
    
    template = jinja_environment.get_template('views/results.html')
    self.response.out.write(template.render(template_values))

routes = [('/', HomeHandler),('/results', ResultsHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 