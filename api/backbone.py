import os
import json
import sys
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def queryDomain_precheck(domain):
    if not (domain.endswith(".eu")):
        return True
    else:
        return False

def queryDomainRun(domain):
    if (sys.platform == "win32"):
        #cmd = "whois64.exe -v %s" % domain
        cmd = BASE_DIR+"\whois64.exe -v %s" % domain
    else:
        #print(sys.platform)
        cmd = "whois %s" % domain
    a = os.popen(cmd).read()
    return a

#function to break down str to list
def stringsplitcolon(inputstring):
    myresult = []
    for line in inputstring.splitlines():
        if (": " in line):
            subline = re.split(": ",line)
            #clean up strings
            subline_result = [x.strip(' ') for x in subline]
            myresult.append(subline_result)
    return myresult

def queryDomain(domain,format="json"):
    if (queryDomain_precheck(domain)):
        result = queryDomainRun(domain)
        result_list = stringsplitcolon(result)
        result_json = json.dumps(result_list, indent=4)
        if (format == "json"):
            return result_json
        elif (format == "raw"):
            return result
        elif format == "dict":
            dictdump = json.loads(result_json)
            return dictdump
        else:
            return None
    else:
        return "Unsupported domain"

#result = queryDomain("alnet.se")
#print(result)
#print(BASE_DIR)