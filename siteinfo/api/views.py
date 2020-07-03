from rest_framework import viewsets
from .serializers import SiteSerializer
from .models import Site
from django.shortcuts import render
from .backbone import queryDomain
from django.template.defaulttags import register

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer

def sitelist(request):
    result = Site.objects.all().order_by('name')
    return render(request, 'api/list.html',{'results':result, 'title':'sitelist'})

def whois(request, siteurl):
    if siteurl:
        try:
            result_json = queryDomain(siteurl, format="dict")
            return render(request, 'api/whois.html',{'siteurl': siteurl,
                                                      'results': result_json,
                                                      'type': type(result_json),
                                                      'count': len(result_json),
                                                      'title': "Whois"})
        except:
            print("Couldn't get it")
            error = "Couldn't get it"
            return render(request, 'api/whois.html',{'siteurl': siteurl, 'results': result_json, 'error_message':error})

        
    else:
        return render(request, 'api/whois.html', {
            'siteurl': siteurl,
            'error_message': "Something went wrong",
        })

def test(request):
    return render(request, 'api/test.html')



@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

