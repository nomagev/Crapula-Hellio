'''
CrapulaHellio.py  is  a  simple, prompt-based
Python-3 written program, to  scan & clean
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
    #import urllib.parse
    #import re
    import sys
except ImportWarning as warning:
    print(str(warning))
    sys.exit()

# Enter URL
WEB_URL = input("Enter Full URL: ")
url = WEB_URL

# Create flow to get website (if error, message will be displayed)
try:
    webHeaders = {}
    # pylint: disable=line-too-long
    webHeaders['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    # pylint: enable=line-too-long
    webRequest = urllib.request.Request(url, headers=webHeaders)
    webResponse = urllib.request.urlopen(url)
    webData = webResponse.read()
    print(webData)
except Exception as error:
    print(str(error))


# Find text between HTML "headline" tags
#headlines = re.findall(r'<h1>(.*?)</h1>', str(respData))

# Get the headlines from the indicated site
#for allHeadlines in headlines:
#    print(allHeadlines)

# End of Program
