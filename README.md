# siteinfo
 site scanner tool built in django

deploy to docker with docker-compose
<site>/list - shows added sites
<site>/add - adds site
<site>/api - shows api
<site/startscan - initates full scan 
<site>/whois/www.mydomain.com - runs whois on address
<site>/whatis/www.mydomain.com - runs whatis cmsscanner on address using WAD, Web Application Detector https://github.com/CERN-CERT/WAD

To call with rest
To call with restapi using curl
Curl -H 'Accept: application/json; indent=4' -u '<username>:<password>' http://127.0.0.1:8000/api/frameworks/ 
 
REST APIs
/api/providers
/api/frameworks
/api/geoip
/api/sites
