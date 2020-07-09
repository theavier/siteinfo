import os
import logging
import json
from django.core.wsgi import get_wsgi_application
from api.models import Site, Framework, Provider, GeoInfo
from api.backbone import queryDomain, whatis_query
from api.backbone_services import GetHostProvider, ping_geo
from django.utils.encoding import punycode

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "siteinfo.settings")
application = get_wsgi_application()

def scansites():
    # read sites from site
    querySites = Site.objects.all().order_by('name')
    print("Found {0} sites".format(len(querySites)))
    logfile = 'siteinfo.log'
    logging.basicConfig(filename=logfile,level=logging.INFO)
    logging.info('Starting logfile')
    # loop through sites and scan
    for querysite in querySites:
        print("Url: {0}".format(querysite.url))
        url_encoded = punycode(querysite.url)
        print("Encoded url: {0}".format(url_encoded))
        # enter whatis_query result into database
        scan_result = whatis_query(url_encoded)
        print("Count {0}, type: {1}".format(len(scan_result),type(scan_result)))
        scan_json = json.loads(scan_result)
        for key, value in scan_json.items():
            print("Checking site: {0}".format(key))
            print("Type: {0}".format(type(value)))
            for app in value:
                # check if value already exists, then update existing
                app_insertdata = app.copy()
                if not app_insertdata['ver']:
                    app_insertdata['ver'] = "N/A"
                print(app_insertdata)
                try:
                    obj, created = Framework.objects.update_or_create(app=app['app'],site=querysite, defaults=app_insertdata)
                    if created:
                        print('created new databaseentry')
                    elif obj:
                        print('updated existing databasentry')
                    else:
                        print("Couldn't update at all")
                except BaseException as e:
                    print("Couldn't insert: {0}. \n Cause: {1}".format(app_insertdata,e))

        # check provider
        print("Checking provider for {0}".format(url_encoded))
        hostprovider = GetHostProvider(address=url_encoded)
        print("Provider: {0}, Ip: {1}, source: {2}".format(hostprovider.provider,hostprovider.ip
                                                           ,hostprovider.source))
        # add provider to database
        provider_insertdata = {'provider': hostprovider.provider, 'ip': hostprovider.ip, 'source': hostprovider.source}
        try:
            provider_obj, provider_created = Provider.objects.update_or_create(site=querysite, defaults=provider_insertdata)
            if provider_created:
                print('created new providerdatabase for {0}'.format(url_encoded))
            else:
                print('Updated existing providerentry')
        except BaseException as e:
            print("Couldn't insert {0}. \n Cause: {1}".format(provider_insertdata, e))

        # check geodata
        geo_insertdata = ping_geo(url_encoded)
        # add geodata to database
        print(geo_insertdata)
        try:
            geo_obj, geo_created = GeoInfo.objects.update_or_create(site=querysite, defaults=geo_insertdata)
            if provider_created:
                print('created new providerdatabase for {0}'.format(url_encoded))
            else:
                print('Updated existing providerentry')
        except BaseException as e:
            print("Couldn't insert {0}. \n Cause: {1}".format(geo_insertdata, e))
        print("Scansites ended")
