import indicoio
import urllib2
import json
from graph import TrendGraph

indicoio.config.api_key = "ed10971412405df6de77333f9fab3033"
Nyt_Api_Key = "20e826df5fe19554ac6d8d56d9708b23:2:71828824"

def createNewUrl(query, begin_date, end_date, Nyt_Api_Key):
    query = query.replace(" ", "+")
    url =  "http://api.nytimes.com/svc/search/v2/articlesearch.json?"
    url += "q="             + query
    url += "&begin_date="   + begin_date
    url += "&end_date="     + end_date
    url += "&api-key="      + Nyt_Api_Key
    print "Requesting data from NYT URL: " + url
    return url

urlToRequest = createNewUrl("Global Warming", "20000101", "20150411", Nyt_Api_Key)
response_json = json.load(urllib2.urlopen(urlToRequest))

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
    leanings = indicoio.political(snippet_to_analyze)
    
    data['liberal'].append(leanings['Liberal'])
    data['green'].append(leanings['Green'])
    data['conservative'].append(leanings['Conservative'])
    data['libertarian'].append(leanings['Libertarian'])

My_Graph = TrendGraph(data)
My_Graph.getGraph()

#sample_data = {}
#sample_data['dates']         =    ["Year 2010", "Year 2011", "Year 2012", "Year 2013"]
#sample_data['liberals']      =    [0.25, 0.25, 0.25, 0.25]
#sample_data['conservatives'] =    [0.25, 0.25, 0.25, 0.25]
#sample_data['libertarian']   =    [0.25, 0.25, 0.25, 0.25]
#sample_data['green']         =    [0.25, 0.25, 0.25, 0.25]

#my_Graph = TrendGraph(sample_data)

#my_Graph.getGraph()
