from django.shortcuts import render
from courses.models import CourseInfo, SectionInfo
#need to pass classes as JSON objects to be used to generate schedule in javascript
import json
from .forms import RemoveCourseFromSchedule, AddCourseToSchedule

# Create your views here.
def schedule(request):
    user = request.user
    # sending over all courses for the current user
    # sections = CourseInfo.objects.all().filter(sections__students = user)
    user_sections = SectionInfo.objects.all().filter(students=user)
    context = {'sections': user_sections}
    if request.method == 'POST':
        file = open('post.txt','w') 
        file.write('posting') 
        file.close()
        # if the user hit remove course button
        file = open('remove.txt','w') 
        file.write('remove in request') 
        file.close()
        form = RemoveCourseFromSchedule(request.POST)
        if form.is_valid():
            user = request.user
            section = request.POST.getlist('courses[]')
            section_to_remove = SectionInfo.objects.get(id=section[0])
            section_to_remove.students.remove(user)
            context["form"] = form
        else:
            context["form"] = RemoveCourseFromSchedule()

    return render(request,'schedule/schedule.html',context)

