#setup for django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "siteinfo.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from api.models import Site, Framework
#endsetup
from api.backbone import queryDomain, whatis_query
import json


#read sites from site
querySites = Site.objects.all().order_by('name')

#loop through sites and scan
for querysite in querySites:
    print(querysite.url)
    #enter scanresult into database
    scan_result = whatis_query(querysite.url)
    #print(scan_result)
    print("Count {0}, type: {1}".format(len(scan_result),type(scan_result)))
    scan_json = json.loads(scan_result)
    #print(scan_json)
    for key, value in scan_json.items():
        print("Checking site: {0}".format(key))
        #print("Content:")
        #print(value)
        print("Type: {0}".format(type(value)))
        for app in value:
            #check if value already exists, then update existing
            insertdata = app.copy()
            if not insertdata['ver']:
                insertdata['ver'] = "N/A"
            print(insertdata)
            try:
                obj, created = Framework.objects.update_or_create(app=app['app'],site=querysite, defaults=insertdata)
                if created:
                    print('created new databaseentry')
                elif obj:
                    print('updated existing databasentry')
                else:
                    print("Coulnd't update at all")
            except BaseException as e:
                print("Couldn't insert: {0}. \n Cause: {1}".format(insertdata,e))






