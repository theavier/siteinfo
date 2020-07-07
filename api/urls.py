from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sites', views.SiteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('whois/<siteurl>', views.whois, name='whois'),
    path('test/', views.test, name='test'),
    path('list/', views.sitelist, name='sitelist'),
    path('add/', views.site_add, name='add'),
    path('whatis/<siteurl>', views.whatis, name='whatis'),    
]