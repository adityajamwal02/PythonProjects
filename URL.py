"""
URL SHORTENER: INPUT THE DESIRED URL LINK AND 
ACCESS FETCHED DATA USING API TO GET SHORTENED FORMAT
"""


from pyshorteners import Shortener
long_url = 'http://www.google.com'
API_Key = 'ec73ee08d5d04821e36aa99a8aaf9bc67a2499c2'
s = Shortener( api_key = API_Key)
print ("\n Short URL is {}".format(s.bitly.short(long_url)))



"""
URL EXPANDER: INPUT THE DESIRED URL LINK AND 
ACCESS FETCHED DATA USING API TO GET ORIGINAL FORMAT
"""

from pyshorteners import Shortener
short_url = 'https://bit.ly/2XDW2ov'
API_Key = 'ec73ee08d5d04821e36aa99a8aaf9bc67a2499c2'
s = Shortener( api_key = API_Key)
print ("OG URL is {}".format(s.bitly.expand(short_url)))