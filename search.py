import urllib3
import hashlib
import datetime
import urllib.request
from time import strftime, gmtime
from urllib.request import urlopen
# credentials and request params
my_affiliate_id = 2312847
api_token       = 'pp1TTmNJZg6XzcxR'
api_secret_key  = 'KSm7ho5a3NMmly3sBQb0no7f4SZmqf1s'
my_timestamp    = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
api_version     = 2.3
action_verb     = 'merchantDataFeeds'
#action_verb     = 'couponDeals';
modifiedDate  ='04/13/20'
myFormat ='xml'
# setup request params
#this is for the vedors
#data = urllib.parse.urlencode({'affiliateId' : my_affiliate_id, 'token' : api_token, 'version' : api_version, 'action' : action_verb, 'ModifiedDate' :modifiedDate})
#this is for the coupons
#data = urllib.parse.urlencode({'affiliateId' : my_affiliate_id, 'token' : api_token, 'version' : api_version, 'action' : action_verb, 'XMLFormat' : 1,'format' :myFormat, 'ModifiedDate' :modifiedDate})
# authentication
#data = urllib.parse.urlencode({'affiliateId' : my_affiliate_id, 'token' : api_token, 'version' : api_version, 'action' : action_verb, 'XMLFormat' : 1,'format' :myFormat, 'activatedSince' :modifiedDate,'notjoined': 0})
#merchant datfeed
data = urllib.parse.urlencode({'affiliateId' : my_affiliate_id, 'token' : api_token, 'version' : api_version, 'action' : action_verb, 'XMLFormat' : 1,'format' :myFormat, 'blnMemberOf':1})

sig = api_token + ':' + my_timestamp + ':' + action_verb + ':' + api_secret_key;
sig_hash = hashlib.sha256(sig.encode('utf-8')).hexdigest()
#hashlib.sha256("a".encode('utf-8')).hexdigest()
my_headers = {'x-ShareASale-Date' : my_timestamp, 'x-ShareASale-Authentication' : sig_hash}
# execute request
request       = urllib.request.Request('https://api.shareasale.com/x.cfm?%s' % data, headers = my_headers)
return_result = urllib.request.urlopen(request).read()
# output results to console or write to file
#print (return_result)
f = open('search.txt', 'w')
print ( return_result, file=f)
# print >> f, return_result
f.close()