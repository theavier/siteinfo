import os
import json
import sys
import re
import subprocess

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

def whatis_query(domain):
    if not domain.startswith("https") and not domain.startswith("http"):
        domain = "https://"+domain
    if (sys.platform == "linux"):
        cmd = "wad -u "+domain
        try:
            proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True, universal_newlines=True)
            (out, err) = proc.communicate()
            return out
        except:
            return "Something went wrong"+err
    else:
        #return "Unsupported platform"
        fake_data = whatis_fake()
        return fake_data

def whatis_fake():
    file = os.path.join(BASE_DIR, 'fake.json')
    print(file)
    with open(file) as json_file:
        data = json.load(json_file)
    return data

#testresult = whatis_fake()
#print(testresult)
#testresult = whatis_query("www.dataman.se")
#print(testresult)

