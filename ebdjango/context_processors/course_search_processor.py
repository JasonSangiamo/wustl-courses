from courses.models import CourseInfo
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
# always send the list of all courses because the search function in navbar needs them
def return_courses_json(request):
    courses = CourseInfo.objects.all()
    # course_query = CourseInfo.objects.all().values('name','id','department_abbreviation')
    # # courses_json_list = list(course_query.values('name','id','department_abbreviation'))
    return {'all_courses_for_search': courses}
