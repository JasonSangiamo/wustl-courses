from django.conf.urls import url, include
from . import views

urlpatterns = [
    #returning all of the departments
    url(r'^$', views.departments, name='departments'),
    #returning all instances of a specific course
    # url(r'^(?P<dept_abbreviation>.+)/(?P<pk>\d+)', views.return_course_info, name="return_course_info"),
    #returning the courses for a specific department
    url(r'^(?P<dept_abbreviation>.+)/$', views.department_courses, name = 'department_courses'),
]