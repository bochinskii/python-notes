import urllib.request, urllib.parse, sys

URL = 'https://www.google.com/search?'

QUERY = {
    'q': 'HIM'
}
QUERY_ENCODED = urllib.parse.urlencode(QUERY)

HEADERS = {}
HEADERS['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'

URL = URL + QUERY_ENCODED
PREPERE_REQUEST = urllib.request.Request(URL, headers=HEADERS)
REQUEST = urllib.request.urlopen(PREPERE_REQUEST)

for i in REQUEST.readlines():
    print(i)