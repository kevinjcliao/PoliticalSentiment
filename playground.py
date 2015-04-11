import indicoio
import urllib2

indicoio.config.api_key = "ed10971412405df6de77333f9fab3033"
Nyt_Api_Key = "20e826df5fe19554ac6d8d56d9708b23:2:71828824"

response = urllib2.urlopen('http://api.nytimes.com/svc/search/v2/articlesearch.json?q=Climate+Change&begin_date=20000101&end_date=20150411&api-key='   + Nyt_Api_Key)

html = response.read()

print(html)
