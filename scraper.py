import requests
import lxml.html
import scraperwiki

url = "https://theguardian.com/au"
r = requests.get(url)
dom = lxml.html.fromstring(r.content)
headlines = dom.cssselect(".fc-item__header .js-headline-text")

for headline in headlines:
	data = {}
	data['headline'] = headline.text
	print data
	scraperwiki.sqlite.save(unique_keys=["headline"], data=data, table_name="headlines")