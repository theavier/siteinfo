import requests
import json 
ip = '81.170.175.179'
ipArin = '192.0.78.9'

class ping_ripe: 
    def __init__(self,ip):
        url = 'http://rest.db.ripe.net/search.json?query-string='        
        uri = url+ip                
        response = requests.get(uri)        
        data = json.loads(response.text)        
        self.provider = data['objects']['object'][2]['attributes']['attribute'][1]['value']
    

class ping_arin:
    def __init__(self,ip):
        url = "http://whois.arin.net/rest/ip/"
        uri = url+ip
        response = requests.get(uri,headers={"accept":"application/json"})
        data = json.loads(response.text)
        self.provider = data['net']['orgRef']['@name']
        
        

result2 = ping_arin(ip)
print(result2.provider)
if "RIPE" in result2.provider:
    result = ping_ripe(ip)
    print(result.provider)
else:
    print(result2.provider)
