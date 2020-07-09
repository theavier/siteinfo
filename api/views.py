from rest_framework import viewsets
from .serializers import SiteSerializer, FrameworkSerializer
from .models import Site, Framework
from .forms import AddSite
from django.shortcuts import render, redirect
from .backbone import queryDomain, whatis_query
from django.template.defaulttags import register
from .scansites import scansites

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all().order_by('name')
    serializer_class = SiteSerializer

class FrameworkViewSet(viewsets.ModelViewSet):
    queryset = Framework.objects.all().order_by('site')
    serializer_class = FrameworkSerializer

def sitelist(request):
    result = Site.objects.all().order_by('name')
    return render(request, 'api/list.html',{'results':result, 'title':'sitelist'})

def site_add(request):
    add = AddSite()
    if request.method == 'POST':
        add = AddSite(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('sitelist')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'api/add_form.html', {'add_form':add})

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

def whatis(request, siteurl):
    if siteurl:
        result_json = whatis_query(siteurl)
        return render(request, 'api/whatis.html', {'title':'Whatis','results': result_json})
    

def test(request):
    return render(request, 'api/test.html')


def startscan(request):
    results = scansites()
    error = None
    results = "Scan has run..."
    return render(request, 'api/result.html', {'error': error, 'results': results})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

