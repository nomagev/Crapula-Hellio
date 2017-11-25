'''
CrapulaHellio.py is a simple, prompt-based
Python-3  written program, to scan & clean
news websites to just get the headlines.
'''

__version__ = '0.0.1'
__author__ = 'nomagev'
__maintainer__ = "nomagev"
__license__ = "GPL 2.0"
__email__ = "vegamontesino@msn.com"
__status__ = "Development"

# -*- coding: utf-8 -*-

# Import urllib (request, parse) and re library modules
# Print Import Warning in case of Issue
try:
    import urllib.request
    import urllib.parse
    import re
    import sys
except ImportWarning as warning:
    print(str(warning))
    sys.exit()

# Enter URL to fetch from
WEB_URL = input("Enter Full URL (i.e. www.example.com): ")
url = "http://" + WEB_URL

# Create flow to get website's HTML Code
# (if error, message will be displayed)
try:
    webheaders = {}
    # pylint: disable=line-too-long
    webheaders['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    # pylint: enable=line-too-long
    webrequest = urllib.request.Request(url, headers=webheaders)
    webresponse = urllib.request.urlopen(url)
    webdata = webresponse.read()
    print(webdata)
except Exception as error:
    print(str(error))


# Find text between HTML "headline" tags
headlines = re.findall(r'<h1>(.*?)</h1>', str(respData))

# Get the headlines from the indicated site
for allheadlines in headlines:
    print(allheadlines)

# End of Program
