from __future__ import print_function

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

try:
    x = urlopen("https://google.com").read()
    print(x)
except Exception as e:
    print(str(e))