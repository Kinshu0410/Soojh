from pymongo import MongoClient
#import dns

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception
client=MongoClient('mongodb+srv://Kinshu04101:Qwert123@cluster0.ckcyx.mongodb.net/test?retryWrites=true&w=majority')

import re
qN="psy-02"
col=client["QuizC"][qN]
ll1=col.count_documents({"cor":{"$type":"string"}})
print(ll1)
ll=col.find({"cor":{"$type":"string"}})
cor1={}
var1=1
for x in ll:
	cor1[str(var1)]=x["cor"]
	var1+=1
print(cor1)
coll=client["QuizCData"][qN]
ll=coll.find()
print(coll.count_documents({}))
result={}
for x in range(coll.count_documents({})):
	uid=ll[x]["uid"]
	Z=0
	
	for y in range(ll1):
		try:
			if ll[x][str(y+1)]==cor1[str(y+1)]:
				Z+=4
			else:
				Z-=1
		except:
			pass
	result[uid]=Z
	print(result)
print(result)
		
	
