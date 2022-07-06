import urllib.request

URL = 'https://www.7-zip.org/a/7z2200-linux-x64.tar.xz'
PATH = './7z2200-linux-x64.tar.xz'

urllib.request.urlretrieve(URL, PATH)