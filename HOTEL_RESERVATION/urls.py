from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings

from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Hotel.urls')),
    # path('hotel/', include('Hotel.urls')),
    path('sy-admin/', include('Systemadmin.urls')),
    path('hotel-admin/', include('Hoteladmin.urls')),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
