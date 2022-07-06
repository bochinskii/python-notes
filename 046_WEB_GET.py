import urllib.request

URL = 'http://planetarium.dn.ua'
REQUEST = urllib.request.urlopen(URL)

for i in REQUEST.readlines():
    print(i)