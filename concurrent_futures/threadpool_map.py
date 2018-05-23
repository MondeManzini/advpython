import concurrent.futures
import urllib
 
URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.news24.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/'
]
 
# Retrieve a single page and report the url and contents
def load_url(url, timeout):
    conn =  urllib.urlopen(url)
    return conn.read()
def execute_urls(): 
    # We can use a with statement to ensure threads are cleaned up promptly'
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
	# Start the load operations and mark each future with its URL
	future_to_url = {executor.submit(load_url, url, 60):url for url in URLS}
	for future in concurrent.futures.as_completed(future_to_url):
	    url = future_to_url[future]
	    try:
		data = future.result()
	    except Exception as exc:
		print('%r generated an exception: %s' % (url,exc))
	    else:
		print('%r page is %d bytes' % (url,len(data)))

def linear_urls():
   for url in URLS:
     try:
     	data = urllib.urlopen(url).read()
     except  Exception as exc:
	print('%r generated an exception: %s' % (url,exc))
     else:
	print('%r page is %d bytes' % (url,len(data)))
