from awewards import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.conf import settings


urlpatterns=[
    url(r'^$', views.register),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^home/$',views.welcome, name="welcome"),
    url(r'profile/',views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
