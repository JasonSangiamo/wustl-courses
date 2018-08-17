from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('home.urls'),name="home"),
    url(r'^courses/', include('courses.urls'),name="courses"),
    url(r'^schedule/', include('schedule.urls'),name="schedule"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
]
