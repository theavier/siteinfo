import requests
import json
import socket


class PingRipe:
    def __init__(self,ip):
        url = 'http://rest.db.ripe.net/search.json?query-string='        
        uri = url+ip                
        response = requests.get(uri)        
        data = json.loads(response.text)        
        self.provider = data['objects']['object'][2]['attributes']['attribute'][1]['value']
        self.source = "Ripe"


class PingArin:
    def __init__(self, ip):
        url = "http://whois.arin.net/rest/ip/"
        uri = url + ip
        response = requests.get(uri, headers={"accept": "application/json"})
        data = json.loads(response.text)
        self.provider = data['net']['orgRef']['@name']
        self.source = "Arin"


def get_ip(urladdress):
    if urladdress.startswith("https://"):
        urladdress = urladdress.replace("https://", "")
    elif urladdress.startswith("http://"):
        urladdress = urladdress.replace("http://", "")
    try:
        hostname = socket.gethostbyname(urladdress)
        return hostname, True
    except BaseException as e:
        return "N/A, Error: "+str(e), False


class GetHostProvider:
    def __init__(self, ip=None, address=None):
        noip = False
        if ip:
            self.ip = ip
        elif address:
            _get_ip, _get_ip_valid = get_ip(address)
            if _get_ip_valid:
                self.ip = _get_ip
            else:
                noip = True
        if not noip:
            result = PingArin(self.ip)
            if "RIPE" in result.provider:
                result = PingRipe(self.ip)
            self.provider = result.provider
            self.source = result.source
        else:
            self.provider = "N/A"
            self.source = "N/A"
            self.ip = "N/A"


def ping_geo(address):
    _ip, _ip_valid = get_ip(address)
    url = "http://www.geoplugin.net/json.gp?ip="
    uri = url + _ip
    response = requests.get(uri, headers={"accept": "application/json"})
    data = json.loads(response.text)
    return_data = {'city': data['geoplugin_city'],
                   'countrycode': data['geoplugin_countryCode'],
                   'country': data['geoplugin_countryName'],
                   'latitude': data['geoplugin_latitude'],
                   'longitude': data['geoplugin_longitude']}
    return return_data

