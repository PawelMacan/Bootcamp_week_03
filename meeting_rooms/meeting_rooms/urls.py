"""meeting_rooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from reservation.views import AddRoom, AllRooms, Modify, Delete, ReserveRoom



urlpatterns = [
    url(r'^room/modify/(?P<id>\d+)$', csrf_exempt(Modify.as_view()), name="modify_go"),
    url(r'^admin/', admin.site.urls),
    url(r'^room/new/$', csrf_exempt(AddRoom.as_view()), name="add_room"),
    url(r'^room$', csrf_exempt(AllRooms.as_view()), name="index"),
    url(r'^$', csrf_exempt(AllRooms.as_view()), name="index"),
    url(r'^(?P<id>\d+)$', csrf_exempt(Delete.as_view()), name="delete"),
    url(r'^room/(?P<id>\d+)$', csrf_exempt(ReserveRoom.as_view()), name="reserve")
]
