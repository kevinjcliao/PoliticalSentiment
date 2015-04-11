import indicoio
import urllib2
import json

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
response = urllib2.urlopen(urlToRequest)

html = response.read()

print(html)
