"""StudentMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from mgmt.views import home,Detail,ParentFormView,StaffFormView,UserFormView,FacultyFormView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', FacultyFormView.as_view(), name='index'),
    url(r'register$', UserFormView.as_view(), name='register'),
    url(r'index.html$', FacultyFormView.as_view(), name='index'),
    url(r'login$', FacultyFormView.as_view(), name='login_user'),
    url(r'register/(?P<id>[0-9]+)$', ParentFormView.as_view(), name='parentform'),
    url(r'register/(?P<id>[0-9]+)$', StaffFormView.as_view(), name='staffform'),
    url(r'register/(?P<id>[0-9]+)$', FacultyFormView.as_view(), name='teacherform'),
    url(r'(?P<username>[a-z0-9]+)$', Detail.as_view(), name='detail'),
]



urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


