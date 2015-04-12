import indicoio
import webapp2
import jinja2
import logging
import os
import urllib2
import json
import requests as r
import ast
#from graph import TrendGraph

Nyt_Api_Key = Nyt_Api_Key = "20e826df5fe19554ac6d8d56d9708b23:2:71828824"
indicoio.config.api_key = "ed10971412405df6de77333f9fab3033"

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

        for x in range(0, len(response_json["response"]["docs"])):
            article_to_analyze = response_json["response"]["docs"][x]
            data['dates'].append(article_to_analyze["pub_date"])

            snippet_to_analyze = article_to_analyze["lead_paragraph"]
            if snippet_to_analyze == None:
                snippet_to_analyze = response_json["response"]["docs"][x]["snippet"]
            #leanings = indicoio.political(snippet_to_analyze)
            leanings = self.postRequest(snippet_to_analyze)

            data['liberal'].append(leanings['Liberal'])
            data['green'].append(leanings['Green'])
            data['conservative'].append(leanings['Conservative'])
            data['libertarian'].append(leanings['Libertarian'])

        #My_Graph = graph.TrendGraph(data)
        #print My_Graph.getGraphImage()

    def postRequest(self, input_snippet): 
        m = r.post('http://apiv1.indico.io/political',
                    json.dumps({'data':input_snippet}))
        u = ast.literal_eval(m.content)
        return u['results']


routes = [('/', HomeHandler),('/results', ResultsHandler)]
app = webapp2.WSGIApplication(routes, debug=True) 
