import indicoio
import webapp2
import jinja2
import logging
import os
import urllib2
import json


Nyt_Api_Key = Nyt_Api_Key = "20e826df5fe19554ac6d8d56d9708b23:2:71828824"


jinja_environment = jinja2.Environment(loader=
        jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                }

        template = jinja_environment.get_template('views/index.html')
        self.response.out.write(template.render(template_values))

class ResultsHandler(webapp2.RequestHandler):
    def createNewUrl(self, query, begin_date, end_date, Nyt_Api_Key):
        query = query.replace(" ", "+")
        url =  "http://api.nytimes.com/svc/search/v2/articlesearch.json?"
        url += "q="             + query
        url += "&begin_date="   + begin_date
        url += "&end_date="     + end_date
        url += "&api-key="      + Nyt_Api_Key
        print "Requesting data from NYT URL: " + url
        return url

    def get(self):  
        template_values = {
                }
        topic = self.request.get('topic')
        template_values['topic'] = topic
        originalstartdate = self.request.get('startdate').split('/')
        startdate = originalstartdate[2] + originalstartdate[1] + originalstartdate[0]
        template_values['startdate'] = startdate

        originalenddate = self.request.get('enddate').split('/')
        enddate = originalenddate[2] + originalenddate[1] + originalenddate[0]
        template_values['enddate'] = enddate

        template = jinja_environment.get_template('views/results.html')
        self.response.out.write(template.render(template_values))

        print startdate
        print enddate
        print topic

        urlToRequest = self.createNewUrl(topic, startdate, enddate, Nyt_Api_Key)
        response_json = json.load(urllib2.urlopen(urlToRequest))
        print "Response from NYT received!"

        data = {
                'dates':[],
                'liberal':[],
                'conservative':[],
                'libertarian':[],
                'green':[]
        }


routes = [('/', HomeHandler),('/results', ResultsHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 
