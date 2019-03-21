"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from oldboy import views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^index.html$', views.index),
    url(r'^course.html$', views.course),
    url(r'^get_course.html$', views.get_course),
    url(r'video-(?P<classification_id>(\d+))-(?P<level_id>(\d+))-(?P<status>(\d+)).html$', views.video),
    url(r'video2-(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+)).html$', views.video2,name='video2'),
    url(r'^aboutUs.html$', views.aboutUs),
    url(r'^teachers.html$', views.teachers),
    url(r'^students.html$', views.students),
    url(r'^more_info.html$', views.more_info),
]
