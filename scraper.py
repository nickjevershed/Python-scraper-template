import requests
import lxml.html
import scraperwiki

# The website you want to scrape
url = "https://theguardian.com/au"

# Fetching the URL with requests
r = requests.get(url)

# Parsing the website content with lxml
dom = lxml.html.fromstring(r.content)

# Lets get all the headlines on the page - use the inspect element tool in your browser to find the right combination of css selections
headlines = dom.cssselect(".fc-item__header .js-headline-text")

# Now we want to go through out list of headline elements and add their text to our database
for headline in headlines:
	data = {}
	data['headline'] = headline.text
	print data

	# Save the data in an sqlite database, with the headline itself as the unique key
	scraperwiki.sqlite.save(unique_keys=["headline"], data=data, table_name="headlines")