from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from awewards import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('awewards.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
